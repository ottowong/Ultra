$(document).ready(function () {
    // when a div with the class "button" is clicked, toggle visibility of all divs with class "button" and id "form"
    $(".allitemsbutton").click(function() {
	    $(".shirt").show();
        $(".hat").show();
        $(".hoodie").show();
        $(".crewneck").show();
	});
    $(".shirtbutton").click(function() {
	    $(".shirt").show();
        $(".hat").hide();
        $(".hoodie").hide();
        $(".crewneck").hide();
	});
    $(".hatbutton").click(function() {
	    $(".shirt").hide();
        $(".hat").show();
        $(".hoodie").hide();
        $(".crewneck").hide();
	});
    $(".hoodiebutton").click(function() {
	    $(".shirt").hide();
        $(".hat").hide();
        $(".hoodie").show();
        $(".crewneck").hide();
	});
    $(".crewneckbutton").click(function() {
	    $(".shirt").hide();
        $(".hat").hide();
        $(".hoodie").hide();
        $(".crewneck").show();
	});
});
