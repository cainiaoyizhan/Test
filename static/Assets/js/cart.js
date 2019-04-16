$(function (){

	countItem();



// <p class="price">&yen;188</p>
// <p class="count">
// 	<a href="javascript:void(0)" class="minus">-</a>
// 	<input type="text" value="1">
// 	<a href="javascript:void(0)" class="add">+</a>
// </p>
// <p class="sum">
// 	<b>&yen;188</b>
// </p>
	//3. 数量加减

	$('.add').click(function (){

		//取前一个兄弟元素的文本内容
		var value = Number($(this).prev().val());
		// console.log(value)
		//var res = value ++;
		$(this).prev().val(++value);
		//价格联动
		//单价
		var priceStr = $(this).parent().parent().next().children().html(); //$188
		// console.log(priceStr)
		//数值
		var price = Number(priceStr.substring(1));
		// console.log(price)
		//小计 <b>&yen;188</b>
		$(this).parent().parent().next().next().html("<em>&yen;"+value*price+"</em>");
		countItem();

	})

	$(".minus").click(function (){
		//取后一个兄弟元素
		var value = Number($(this).next().val());
		//value > 1才能做减法
		if(value > 1){
			$(this).next().val(--value);
		}
		//价格联动
		//单价
		var priceStr = $(this).parent().parent().next().children().html(); //$188
		//数值
		var price = Number(priceStr.substring(1));
		//小计 <b>&yen;188</b>
		$(this).parent().parent().next().next().html("<em>&yen;"+value*price+"</em>");
		countItem();
	})
	//输入数量,失去焦点时价格联动
	$(".count input").blur(function (){
		//数量
		var value = Number($(this).val());
		console.log(value)
		//单价
		var priceStr = $(this).parent().parent().next().children().html(); //$188
		//数值
		var price = Number(priceStr.substring(1));
		//小计 <b>&yen;188</b>
		$(this).parent().parent().next().next().html("<b>&yen;"+value*price+"</b>");
		countItem();
	})
	// 4. 移除商品
	$(".g-item .action").click(function (){

		//点击哪个商品栏,移除当前信息

		$(this).parent().remove();

		countItem();

	})

	

	//5. 总价格和总数量计算

	function countItem(){
		var sum = 0;
		var sumPrice = 0;
		//1. 每一类商品数量和总价
		$("[name=check]").each(function (){
			//获取当前商品的数量和小计
			sum += Number($(this).children('p').children('input').val());
			console.log($(this).children('p').children('input').val())
			var priceStr = $(this).next().next().children().html();
			var price = Number(priceStr.substring(1));
			console.log(priceStr,price)
			sumPrice += price;
		})
		//2. 显示在工具栏
		$("#select_ok").html('已选:<b>'+sum+'</b>件');
		$("#total_ok").html("总计：<b>￥"+sumPrice+'</b>');
	}
})