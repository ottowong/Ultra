// $(document).ready(function () {
//     // when a div with the class "button" is clicked, toggle visibility of all divs with class "button" and id "form"
//     $(".allitemsbutton").click(function() {
// 	    $(".shirt").show();
//         $(".hat").show();
//         $(".hoodie").show();
//         $(".crewneck").show();
// 	});
//     $(".shirtbutton").click(function() {
// 	    $(".shirt").show();
//         $(".hat").hide();
//         $(".hoodie").hide();
//         $(".crewneck").hide();
// 	});
//     $(".hatbutton").click(function() {
// 	    $(".shirt").hide();
//         $(".hat").show();
//         $(".hoodie").hide();
//         $(".crewneck").hide();
// 	});
//     $(".hoodiebutton").click(function() {
// 	    $(".shirt").hide();
//         $(".hat").hide();
//         $(".hoodie").show();
//         $(".crewneck").hide();
// 	});
//     $(".crewneckbutton").click(function() {
// 	    $(".shirt").hide();
//         $(".hat").hide();
//         $(".hoodie").hide();
//         $(".crewneck").show();
// 	});
// });

$(document).ready(function () {
		    $(".allitemsbutton").click(function() {
			    $(".Crewneck").show();
			    $(".Hoodie").show();
			    $(".Hat").show();
			    $(".Shirt").show();
			});

		    $(".Crewneckbutton").click(function() {

                $(".Crewneck").show();
                $(".Hoodie").hide();
                $(".Hat").hide();
                $(".Shirt").hide();
			});
		    $(".Hoodiebutton").click(function() {

                $(".Crewneck").hide();
                $(".Hoodie").show();
                $(".Hat").hide();
                $(".Shirt").hide();
			});
		    $(".Hatbutton").click(function() {

                $(".Crewneck").hide();
                $(".Hoodie").hide();
                $(".Hat").show();
                $(".Shirt").hide();
			});
		    $(".Shirtbutton").click(function() {

                $(".Crewneck").hide();
                $(".Hoodie").hide();
                $(".Hat").hide();
                $(".Shirt").show();
			});

		});
