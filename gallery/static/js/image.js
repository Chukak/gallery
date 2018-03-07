$(document).ready(function() {
    // event click on small image
    $(document).on('click', ".image", function() {
	    var img = $(this);
	    // get path from img
		var src = img.attr('src');
		// delete old popup div if it exists
		$("body").remove("div.popup")
		// add in body
		// add coordinates and simple background
		$("body").append("<div class='popup'>"+
		                 "<div class='popup_bg' style='top:" + img.offset().top /1.5 + "px;'></div>"+
						 "<img src='"+src+"' class='popup_img' style='top:" + img.offset().top /1.5 + "px;'/>"+
						 "</div>");
		// low show
		$(".popup").fadeIn(500);
		// event in background
		$(".popup_bg").click(function(){
		    // delete image
			$(".popup").fadeOut(500);
			setTimeout(function() {
			  $(".popup").remove();
			}, 500);
		});
	});

});