// Main Menu
$(document).on('click', function(ev){
	$('[gl-attr=hidden-click-anywhere]').removeClass('active');
});
$(document).on('click', '[gl-attr=hidden-click-anywhere]', function(ev){
	ev.stopPropagation();
});
$(document).on('click', '[gl-click=main-menu]', function(ev){
	ev.preventDefault();
	if (!$('body').hasClass('with-menu')) {
		$('body').addClass('with-menu');
	} else {
		$('body').removeClass('with-menu');
	}
});

$(document).on('click', '[gl-click=user-options]', function(ev){
	ev.stopPropagation();
	$(this).parent().toggleClass('active');
});

$(document).on('click', '[gl-function=main-list] a', function(ev){
	$parent_li = $(this).parent();
	$parent_li.siblings().removeClass('active');
	$parent_li.siblings().find('.active').removeClass('active');
	$parent_li.toggleClass('active');
});