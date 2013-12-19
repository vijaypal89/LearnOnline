     $(function () {
            $('.showTip').tip();  
        });

        /* Tooltip plug-in */
        (function ($) {
            $.fn.extend({
                tip: function (options) {
                    var defaults = {
                        maxWidth: '400px',
                        offset: 20,
                        theme: 'blueTip'
                    };

                    /*
                    extend the options
                    */
                    var options = $.extend(defaults, options);

                    return this.each(function () {
                        var o = options;
                        var instance = $(this);
                        var theme = o.theme;

                        instance.hover(function () {
                            var item = $(this);
                            tip = $('<div id=\'tip\'><p>' + item.attr('alt') + '</p></div>');
                            tip.addClass(o.theme).appendTo('body');
                            tip.show();
                        },

				function () {
				    tip.hide();
				}).mousemove(function (e) {

				    var offset = 20;
				    var xCord = e.pageX + offset; //Get X coodrinates
				    var yCord = e.pageY + offset; //Get Y coordinates
				    if (typeof tip != 'undefined') {
				        var tipWidth = tip.width(); //Find width of tooltip
				        if (tip.width() > parseInt(o.maxWidth, 10)) {
				            tip.width(o.maxWidth);
				        }

				        var tipHeight = tip.height(); //Find height of tooltip
				        var distFromRight = $(window).width() - (xCord + tipWidth);
				        var disFromBottom = $(window).height() - (yCord + tipHeight);

				        //If there is not enough space on the right or bottom side just flip it
				        if (distFromRight < offset) {
				            xCord = e.pageX - tipWidth - offset;
				        } if (disFromBottom < offset) {
				            yCord = e.pageY - tipHeight - offset;
				        }
				        tip.css({ left: xCord, top: yCord });
				    }
				});
                    });
                }
            });
        })(jQuery);
    
