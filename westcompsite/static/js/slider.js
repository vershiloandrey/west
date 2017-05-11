$(document).ready(function () {
            $(".slider").each(function () {

                var repeats = 5, // кількість повторювань автоматичного прокручування
                    interval = 10, // інтервал в секундах
                    repeat = true, // чи треба автоматично прокручувати (true/false)
                    slider = $(this),
                    repeatCount = 0,
                    elements = $(slider).find("li").length;

                $(slider)
                    .append("<div class='nav'></div>")
                    .find("li").each(function () {
                    $(slider).find(".nav").append("<span data-slide='" + $(this).index() + "'></span>");
                    $(this).attr("data-slide", $(this).index());
                })
                    .end()
                    .find("span").first().addClass("on");

                // add timeout

                if (repeat) {
                    repeat = setInterval(function () {
                        if (repeatCount >= repeats - 1) {
                            window.clearInterval(repeat);
                        }

                        var index = $(slider).find('.on').data("slide"),
                            nextIndex = index + 1 < elements ? index + 1 : 0;

                        sliderJS(nextIndex, slider);

                        repeatCount += 1;
                    }, interval * 1000);
                }

            });


            // для второго слайдера
            $(".slider2").each(function () {

                var repeats = 5, // кількість повторювань автоматичного прокручування
                    interval = 10, // інтервал в секундах
                    repeat = true, // чи треба автоматично прокручувати (true/false)
                    slider2 = $(this),
                    repeatCount = 0,
                    elements = $(slider2).find("li").length;

                $(slider2)
                    .append("<div class='nav'></div>")
                    .find("li").each(function () {
                    $(slider2).find(".nav").append("<span data-slide='" + $(this).index() + "'></span>");
                    $(this).attr("data-slide", $(this).index());
                })
                    .end()
                    .find("span").first().addClass("on");

                // add timeout

                if (repeat) {
                    repeat = setInterval(function () {
                        if (repeatCount >= repeats - 1) {
                            window.clearInterval(repeat);
                        }

                        var index = $(slider2).find('.on').data("slide"),
                            nextIndex = index + 1 < elements ? index + 1 : 0;

                        sliderJS2(nextIndex, slider2);

                        repeatCount += 1;
                    }, interval * 1000);
                }

            });

        });


        function sliderJS(index, slider) { // slide
            var ul = $(slider).find("ul"),
                bl = $(slider).find("li[data-slide=" + index + "]"),
                step = $(bl).width();

            $(slider)
                .find("span").removeClass("on")
                .end()
                .find("span[data-slide=" + index + "]").addClass("on");

            $(ul).animate({
                marginLeft: "-" + step * index
            }, 500);
        }

        $(document).on("click", ".slider .nav span", function (e) { // slider click navigate
            e.preventDefault();
            var slider = $(this).closest(".slider"),
                index = $(this).data("slide");

            sliderJS(index, slider);
        });


        function sliderJS2(index, slider2) { // slide
            var ul = $(slider2).find("ul"),
                bl = $(slider2).find("li[data-slide=" + index + "]"),
                step = $(bl).width();

            $(slider2)
                .find("span").removeClass("on")
                .end()
                .find("span[data-slide=" + index + "]").addClass("on");

            $(ul).animate({
                marginLeft: "-" + step * index
            }, 500);
        }

        $(document).on("click", ".slider2 .nav span", function (e) { // slider click navigate
            e.preventDefault();
            var slider2 = $(this).closest(".slider2"),
                index = $(this).data("slide");

            sliderJS2(index, slider2);
        });
