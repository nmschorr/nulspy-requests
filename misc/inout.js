/**
   * 获取inputs 、 outputs
   * @param transferInfo
   * @param balanceInfo
   * @param type
   * @returns {*}
   * nms: from: https://github.com/nuls-io/nuls-v2-js-sdk/blob/d6ca8704544fe63db03a678e19b0e22a915c0d5b/src/test/api/util.js
   */

// https://github.com/nuls-io/nuls-v2-js-sdk/blob/d6ca8704544fe63db03a678e19b0e22a915c0d5b/lib/test/contractCall.js



  inputsOrOutputs(transferInfo, balanceInfo, type) {
    let newAmount = transferInfo.amount + transferInfo.fee;
    let newLocked = 0;
    let newNonce = balanceInfo.nonce;
    let newoutputAmount = transferInfo.amount;
    let newLockTime = 0;
    if (balanceInfo.balance < transferInfo.amount + transferInfo.fee) {
      return {success: false, data: "Your balance is not enough."}
    }
    if (type === 4) {
      newLockTime = -1;
    } else if (type === 5) {
      newLockTime = -1;
    } else if (type === 6) {
      newAmount = transferInfo.amount;
      newLocked = -1;
      newNonce = transferInfo.depositHash.substring(transferInfo.depositHash.length - 16);
      newoutputAmount = transferInfo.amount - transferInfo.fee;
    } else if (type === 9) {
      newAmount = transferInfo.amount;
      newLocked = -1;
      newNonce = transferInfo.depositHash.substring(transferInfo.depositHash.length - 16);
      newoutputAmount = transferInfo.amount - transferInfo.fee;
      //锁定三天
      let times = (new Date()).valueOf() + 3600000 * 72;
      newLockTime = Number(times.toString().substr(0, times.toString().length - 3));
    } else {
      //return {success: false, data: "No transaction type"}
    }
    let inputs = [{
      address: transferInfo.fromAddress,
      assetsChainId: transferInfo.assetsChainId,
      assetsId: transferInfo.assetsId,
      amount: newAmount,
      locked: newLocked,
      nonce: newNonce
    }];
    let outputs = [];
    if (type === 15 || type === 17) {
      return {success: true, data: {inputs: inputs, outputs: outputs}};
    }
    if (type === 16) {
      if (!transferInfo.toAddress) {
        return {success: true, data: {inputs: inputs, outputs: outputs}};
      } else {
        newoutputAmount = transferInfo.value;
      }
    }
    // if (newoutputAmount != 0) {
    outputs = [{
      address: transferInfo.toAddress ? transferInfo.toAddress : transferInfo.fromAddress,
      assetsChainId: transferInfo.assetsChainId,
      assetsId: transferInfo.assetsId,
      amount: newoutputAmount,
      lockTime: newLockTime
    }];
    // }
    /*console.log(inputs);
    console.log(outputs);*/
    return {success: true, data: {inputs: inputs, outputs: outputs}};
  },