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
    else if ((trans.appraisal.status === 'INITIATED' || trans.appraisal.status === 'REJECTED_RO' || trans.appraisal.status === "REJECTED_RATEE" ) && trans.appraisal.RateeId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_IO'
        flag = 1
    } 
    else if (trans.appraisal.status === 'APPROVED_IO' && trans.appraisal.ROId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REAPPROVED_RATEE'
        flag = 1
    }
    else if ((trans.appraisal.status === 'REAPPROVED_RATEE' || trans.appraisal.status === 'REJECTED_SRO') && trans.appraisal.SROId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'APPROVED_RO'
        flag = 1
    }
    else if ((trans.appraisal.status === 'APPROVED_RO' || trans.appraisal.status === 'REJECTED_AO') && trans.appraisal.AOId === trans.newOfficer.OfficerId){
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
}

/**
 * Do a rejection
 * @param {org.army.Reject} RejectAppraisal 
 * @transaction
 */
async function Reject(trans) {
    if (trans.appraisal.status === 'INITIATED' && trans.appraisal.RateeId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REJECTED_IO'
    } 
    else if (trans.appraisal.status === 'APPROVED_IO' && trans.appraisal.IOId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REJECTED_RATEE'
    }
    else if (trans.appraisal.status === 'REAPPROVED_RATEE' && trans.appraisal.IOId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REJECTED_RO'
    }
    else if (trans.appraisal.status === 'APPROVED_RO' && trans.appraisal.ROId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REJECTED_SRO'
    }
    else if (trans.appraisal.status === 'APPROVED_SRO' && trans.appraisal.SROId === trans.newOfficer.OfficerId){
        trans.appraisal.officer = trans.newOfficer
        trans.appraisal.status = 'REJECTED_AO'
    }
      
    let assetRegistry = await getAssetRegistry('org.army.Appraisal');
    await assetRegistry.update(trans.appraisal);
}

/**
 * Mark attendance
 * @param {org.army.MarkAttendance} MarksAttendance 
 * @transaction
 */
async function MarkAttendance(trans) {
    trans.attendance.attendance += 1
    let assetRegistry = await getAssetRegistry('org.army.Attendance');
    await assetRegistry.update(trans.attendance);
}
  
  