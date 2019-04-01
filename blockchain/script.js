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
        flag = 1
    }
    else if (trans.appraisal.status === 'INITIATED' && trans.appraisal.RateeId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_IO'
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
        flag = 1
    }
    else if (trans.appraisal.status === 'APPROVED_RO' && trans.appraisal.AOId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_SRO'
        flag = 1
    }
    else if (trans.appraisal.status === 'APPROVED_SRO'){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_AO'
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
    console.log(now)
    nowDate = now.setHours(0,0,0,0)
    console.log(nowDate)
    lastDate = new Date(trans.attendance.currentdate)
    console.log(lastDate)
    lastDate = lastDate.setHours(0,0.0,0)
    console.log(lastDate)
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
    // need to stop backdate leaves
    if ((trans.to > trans.from) && (trans.from > now.toDateString())) {        
        let assetRegistry = await getAssetRegistry('org.army.LeaveRecord');
        await assetRegistry.update(trans.leave);
    }
    else{
        throw new Error("Invalid transaction");
    }
}


// /**
//  * Returns Status
//  * @param {org.army.ViewStatus} ReturnsStatusOfAppraisal 
//  * @transaction
//  */
// No need to implement, officer already has direct read access to his complete appraisal
// async function ViewStatus(trans){
// }
  