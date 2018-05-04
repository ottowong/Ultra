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
