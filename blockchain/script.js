/**
 * Do an approval
 * @param {org.army.Approve} ApproveAppraisal 
 * @transaction
 */
async function Approve(trans) {
    let flag = 0
    if (trans.appraisal.status === 'NONE' && trans.appraisal.IOId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'INITIATED'
        trans.appraisal.remarkRatee = trans.remark
        flag = 1
    }
    else if (trans.appraisal.status === 'INITIATED' && trans.appraisal.RateeId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_IO'
        trans.appraisal.remarkIO = trans.remark
        flag = 1
    } 
    else if (trans.appraisal.status === 'APPROVED_IO' && trans.appraisal.ROId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REAPPROVED_RATEE'
        flag = 1
    }
    else if (trans.appraisal.status === 'REAPPROVED_RATEE' && trans.appraisal.SROId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_RO'
        trans.appraisal.remarkRO = trans.remark
        flag = 1
    }
    else if (trans.appraisal.status === 'APPROVED_RO' && trans.appraisal.AOId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_SRO'
        trans.appraisal.remarkSRO = trans.remark
        flag = 1
    }
    else if (trans.appraisal.status === 'APPROVED_SRO'){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_AO'
        trans.appraisal.remarkAO = trans.remark
        flag = 1
    }

    if (flag){
        let assetRegistry = await getAssetRegistry('org.army.Appraisal');
        await assetRegistry.update(trans.appraisal);
    }
    else{
        throw new Error("Invalid transaction")
    }
}


/**
 * Mark attendance
 * @param {org.army.MarkAttendance} MarksAttendance 
 * @transaction
 */
async function MarkAttendance(trans) {
    var now = new Date()
    // to compare current date with today's date
    // avoid double attendance
    nowDate = now.setHours(0,0,0,0)
    lastDate = new Date(trans.attendance.currentdate)
    lastDate = lastDate.setHours(0,0.0,0)
    if (lastDate < nowDate) {
        trans.attendance.attendance += 1
        trans.attendance.currentdate = now
        let assetRegistry = await getAssetRegistry('org.army.Attendance');
        await assetRegistry.update(trans.attendance);
    }
    else{
        throw new Error("Invalid transaction");
    }

}

/**
 * Mark Leave
 * @param {org.army.MarkLeave} MarkLeave
 * @transaction
 */
async function MarkLeave(trans) {
    var now = new Date()
    nowDate = now.setHours(0,0,0,0)
    fromDate = new Date(trans.leave.from)
    fromDate = fromDate.setHours(0,0,0,0)
    toDate = new Date(trans.leave.to)
    toDate = toDate.setHours(0,0,0,0)

    // need to stop backdate leaves, reject the backdate leaves
    // assumption is that clerk approves the leave just after application received from officer
    if ((toDate > fromDate) && (fromDate > nowDate) && (trans.leave.status != 'REJECTED')) {
        trans.leave.status = 'APPROVED'        
    }
    else{
        trans.leave.status = 'REJECTED'
    }
    let assetRegistry = await getAssetRegistry('org.army.LeaveRecord');
    await assetRegistry.update(trans.leave);
}


// /**
//  * Returns Status
//  * @param {org.army.ViewStatus} ReturnsStatusOfAppraisal 
//  * @transaction
//  */
// No need to implement, officer already has direct read access to his complete appraisal
// async function ViewStatus(trans){
// }
  