Page({
  //页面的初始数据
  data: {
           //导航第一行
    navs2:[{url:"../../images/icon1.png", name:"家电维修"},
            {url:"../../images/icon2.png", name:"家电清洗"},
            {url:"../../images/icon3.png", name:"卫生清洁"},
            {url:"../../images/icon8.png", name:"阿姨/月嫂"},],
             //导航第二行
    navs3:[{url:"../../images/icon4.png", name:"开锁/换锁"},
            {url:"../../images/icon6.png", name:"疏通"},
            {url:"../../images/icon5.png", name:"家电维修"},
            {url:"../../images/icon7.png", name:"更多"},],
     //广告
     ad:[{url:"../../images/reg.png"}]
  },
  //生命周期函数--监听页面加载
  onLoad: function(options) {
    var that=this
    // Do some initialize when page load.
       wx.request({
            url: "http://www.caozaifei.top/sizu/wx_ylx/apl/lunbo.php",
            method:'GET',
            header:{
                "Content-Type":"application/json"
            },
            success: function(res) {
              console.log([res.data]);
              that.setData({"lunbo":[res.data]});
            },
            fail:function(){
              console.log(22222);
            }
          });
  },
  //生命周期函数--监听页面渲染完成
  onReady: function() {
    // Do something when page ready.
  },
  //生命周期函数--监听页面显示
  onShow: function() {
    // Do something when page show.
           
  },
  //生命周期函数--监听页面隐藏
  onHide: function() {
    // Do something when page hide.
  },
  //生命周期函数--监听页面卸载
  onUnload: function() {
    // Do something when page close.
  },
  // Event handler.
  viewTap: function() {
    this.setData({
      text: 'Set some data for updating view.'
    })
  }
})
