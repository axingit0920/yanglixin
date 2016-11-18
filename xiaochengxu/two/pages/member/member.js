Page({
  data: {
     /* member:[{yue:"100",message:"余额"},
            {yue:"50",message:"积分"},
            {yue:"2",message:"优惠券"},],*/
        navs1:[{url:"../../images/i1.png", name:"钱包",dian:">"},
            {url:"../../images/i2.png", name:"服务地址",dian:">"},],
        navs2:[{url:"../../images/i3.png", name:"意见反馈",dian:">"},
            {url:"../../images/i4.png", name:"关于我们",dian:">"},
            {url:"../../images/i5.png", name:"呼叫客服",dian:">"},],
    headerimg: '../../images/tx.png',
    username:'小明'
  },
  imageError: function(e) {
    console.log('image3发生error事件，携带值为', e.detail.errMsg)
  }
})