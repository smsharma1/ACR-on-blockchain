/**
 * New script file
 */
async function Approve(trans) {
    if (trans.officer.designation === 'RATEE'){
      	if (trans.appraisal.status === 'NONE' && trans.appraisal.officer.officerId === ){
          	trans.appraisal.officer = trans.newOfficer
          	trans.appraisal.status = 'INITIATED'
        }
    }
    let assetRegistry = await getAssetRegistry('org.example.mynetwork.Appraisal');
    await assetRegistry.update(trans.appraisal);
}

