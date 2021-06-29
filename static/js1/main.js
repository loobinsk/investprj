let searchClose = true

$('.clients__search-btn').bind('click', function() {

    if (searchClose == true) {
        $(this).parents('.short-search').find('.search__field').fadeIn(500)

        $(this).parents('.short-search').animate({
            width: 177
        }, 500);

        searchClose = false
    } else if (searchClose == false) {
        $(this).parents('.short-search').find('.search__field').fadeOut(500)

        $(this).parents('.short-search').animate({
            width: 16
        }, 500);

        searchClose = true
    }


})

$('.radio-block input[type="radio"]').bind('change', function() {
    if ($(this).prop('checked') && !$(this).parents('.radio-block').find('.radio-block__hidden').hasClass('open-all')) {
        $(this).parents('.card').find('.radio-block__hidden').slideUp(250)
        $(this).parents('.radio-block').find('.radio-block__hidden').slideDown(250)
    } else if (!$(this).prop('checked')) {
        $(this).parents('.radio-block').find('.radio-block__hidden').slideDown(250)
    }
})

function chek1() {
    if ($('#existingClient').prop('checked')) {
        if ($('#clientSelect').val() == "") {
            yeah = 0
            $('#clientSelect').siblings('button').addClass('req')
            setTimeout(function() {
                $('#clientSelect').siblings('button').removeClass('req')
            }, 2000);
        } else {
            yeah = 1
        }
    } else if ($('#newClient').prop('checked')) {
        if (
            $('#nameClient').val() == "") {
            yeah = 0
            $('#nameClient').addClass('req')
            setTimeout(function() {
                $('#nameClient').removeClass('req')
            }, 2000);
        } else {
            yeah = 1
        }
    }
}



$('#next1').bind('click', function() {

    chek1()
    if (yeah == 1) {
        $('.quiz__card_1').fadeOut(1)
        $('.quiz__card_2').fadeIn(500)
        $('#step1').addClass('closed')
        $('#step2').addClass('active')
    } else if (yeah == 0) {

    }

})

$('input[name="clientInfo"]').bind('change', function() {
    // $('#next1').removeClass('active')
    if ($('#existingClient').prop('checked')) {
        if (!$('#clientSelect').val() == "") {
            $('#next1').addClass('active')
        } else if ($('#clientSelect').val() == "") {
            $('#next1').removeClass('active')
        }
    } else if ($('#newClient').prop('checked')) {
        if (!$('#nameClient').val() == "") {
            $('#next1').addClass('active')
        } else if ($('#nameClient').val() == "") {
            $('#next1').removeClass('active')
        }
    }
})



$('#clientSelect').bind('change', function() {
    $('#next1').addClass('active')
})

$('#nameClient').bind('input', function() {
    if (!$(this).val() == "") {
        $('#next1').addClass('active')
    } else {
        $('#next1').removeClass('active')
    }

})



$('#next2').bind('click', function() {
    // if ($('#existingPortfolio').prop('checked')) {
    //     if ($('.added-file').length > 0) {
    //         $('.quiz__card_2').fadeOut(1)
    //         $('.quiz__card_3').fadeIn(500)
    //         $('#step2').addClass('closed')
    //         $('#step3').addClass('active')
    //     } else {}
    // } else if ($('#newPortfolio').prop('checked')) {
        if ($('#investHorizont').val() == "") {
            $('#investHorizont').addClass('req')
            setTimeout(function() {
                $('#investHorizont').removeClass('req')
            }, 2000);
            if ($('#taxPortfolio').prop('checked')) {
                if ($("#typeProfile").val() == "") {
                    $('#typeProfile').siblings('button').addClass('req')
                    setTimeout(function() {
                        $('#typeProfile').siblings('button').removeClass('req')
                    }, 2000);
                }
            }
        } else {
            if ($('#taxPortfolio').prop('checked')) {
                if ($("#typeProfile").val() == "") {
                    $('#typeProfile').siblings('button').addClass('req')
                    setTimeout(function() {
                        $('#typeProfile').siblings('button').removeClass('req')
                    }, 2000);
                } else {
                    $('.quiz__card_2').fadeOut(1)
                    $('.quiz__card_3').fadeIn(500)
                    $('#step2').addClass('closed')
                    $('#step3').addClass('active')
                }
            } else if ($('#cofalifiedPortfolio').prop('checked')) {
                $('.quiz__card_2').fadeOut(1)
                $('.quiz__card_3').fadeIn(500)
                $('#step2').addClass('closed')
                $('#step3').addClass('active')
            }
        }
    // }
})


$('#typeProfile').bind('change', function() {
    if (!$('#investHorizont').val() == "") {
        $('#next2').addClass('active')
    } else {
        $('#next2').removeClass('active')
    }
})

$('#investHorizont').bind('input', function() {
    

    // if ($('#newPortfolio').prop('checked')) {
        if ($('#taxPortfolio').prop('checked')) {
            if (!$('#investHorizont').val() == "" && !$('#typeProfile').val() == "") {
                $('#next2').addClass('active')
            } else {
                $('#next2').removeClass('active')
            }
        } else if ($('#cofalifiedPortfolio').prop('checked')) {
            if (!$('#investHorizont').val() == "") {
                $('#next2').addClass('active')
            } else {
                $('#next2').removeClass('active')
            }
        }
    // }


    // if (!$(this).val() == "" && !$('#typeProfile').val() == "") {

    //     $('#next2').addClass('active')
    // } else {
    //     $('#next2').removeClass('active')
    // }

})

$('#investHorizont').bind('change', function() {
    var txt = $(this).val(),
    count = txt % 100;
    if (count >= 5 && count <= 20) {
        txt = 'лет';
    } else {
        count = count % 10;
        if (count == 1) {
            txt = 'год';
        } else if (count >= 2 && count <= 4) {
            txt = 'года';
        } else {
            txt = 'лет';
        }
    }

    $(this).val($(this).val() + ' ' + txt)
})

$('input[name="typePortfolio"]').bind('change', function() {
    if ($('#cofalifiedPortfolio').prop('checked')) {
        if (!$('#investHorizont').val() == "") {
            $('#next2').addClass('active')
        } else {
            $('#next2').removeClass('active')
        }
    } else if ($('#taxPortfolio').prop('checked')) {
        if (!$('#investHorizont').val() == "" && !$('#typeProfile').val() == "") {
            $('#next2').addClass('active')
        } else {
            $('#next2').removeClass('active')
        }
    }
})


$('#prev2').bind('click', function() {
    $('.quiz__card_2').fadeOut(1)
    $('.quiz__card_1').fadeIn(500)
    $('#step2').removeClass('active')
    $('#step1').removeClass('closed')
    $('#step1').addClass('active')


})


$('#next3').bind('click', function() {


    if (!$('#startCapital').val() == "" &&
        !$('.risk__slider-field').val() == "" &&
        !$('#clientPriority').val() == "") {
        $('.quiz__card_3').fadeOut(1)
        $('.quiz__card_4').fadeIn(500)
        $('#step3').addClass('closed')
        $('#step4').addClass('active')
    } else {
        if ($('#startCapital').val() == "") {
            $('#startCapital').addClass('req')
            setTimeout(function() {
                $('#startCapital').removeClass('req')
            }, 2000);
        }

        // if ($('#fullPortfolioCost').val() == "") {
        //     $('#fullPortfolioCost').addClass('req')
        //     setTimeout(function() {
        //         $('#fullPortfolioCost').removeClass('req')
        //     }, 2000);
        // }

        if ($('.risk__slider-field').val() == "") {
            $('.risk__slider-field').addClass('req')
            setTimeout(function() {
                $('.risk__slider-field').removeClass('req')
            }, 2000);
        }

        if ($('#clientPriority').val() == "") {
            $('#clientPriority').siblings('button').addClass('req')
            setTimeout(function() {
                $('#clientPriority').siblings('button').removeClass('req')
            }, 2000);
        }

        // if ($('#clientVolatility').val() == "") {
        //     $('#clientVolatility').siblings('button').addClass('req')
        //     setTimeout(function() {
        //         $('#clientVolatility').siblings('button').removeClass('req')
        //     }, 2000);
        // }

    }
})


let step3key1, step3key2, step3key3, step3key4, step3key5


function check3() {
    if (step3key1 == 1 &&
        step3key4 == 1) {
        $('#next3').addClass('active')
    } else {
        $('#next3').removeClass('active')
    }
}


$('#startCapital').bind('input', function() {
    if (!$(this).val() == "") {
        step3key1 = 1
    } else {
        step3key1 = 0
    }

    check3();

})

// $('#fullPortfolioCost').bind('input', function() {
//     if (!$(this).val() == "") {
//         step3key2 = 1
//     } else {
//         step3key2 = 0
//     }

//     check3();

// })

$('.risk__slider-field').bind('input', function() {
    if (!$(this).val() == "") {
        step3key3 = 1
    } else {
        step3key3 = 0
    }

    check3();

})


$('#clientPriority').bind('change', function() {
    step3key4 = 1

    check3();
})

// $('#clientVolatility').bind('change', function() {
//     step3key5 = 1
//     check3();
// })

var tooltip = $('<div class="slider-tooltip" id="tooltip" />').css({
    position: 'absolute',
    top: -29,
    left: -6
}).hide();

$("#sliderRisk").each(function() {
    let $this = $(this);
    let min = parseInt($this.data('min'));
    let max = parseInt($this.data('max'));
    $(this).slider({
        animate: true,
        range: "min",
        value: 50,
        min: min,
        max: max,
        step: 1,
        slide: function(event, ui) {
            $(".risk__slider-field").val(ui.value + '%');
            tooltip.text(ui.value);
            if (ui.value >= 0) {
                step3key3 = 1
            } else {
                step3key3 = 0
            }
            check3();

        }
    });


    $(".risk__slider-field").keyup(function() {
        let sum = $(this).val();
        $("#sliderRisk").slider("value", sum);
    });

    $(".risk__slider-field").bind('change', function() {
        $(this).val($(this).val() + '%')
    })

}).find(".ui-slider-handle").append(tooltip).hover(function() {
    tooltip.show()
}, function() {
    tooltip.hide()
})



$('#prev3').bind('click', function() {
    $('.quiz__card_3').fadeOut(1)
    $('.quiz__card_2').fadeIn(500)
    $('#step3').removeClass('active')
    $('#step2').removeClass('closed')
    $('#step2').addClass('active')
})

$('#next4').bind('click', function() {
    if (!$('input[name="types-assets"]:checked').length == 0 && !$('input[name="etf"]:checked').length == 0) {
        $('.quiz__card_4').fadeOut(1)
        $('.quiz__card_5').fadeIn(500)
        $('#step4').addClass('closed')
        $('#step5').addClass('active')


    } else {
        if ($('input[name="types-assets"]:checked').length == 0) {
            $('.quiz__warning_1').addClass('req-text')
        } else {
            $('.quiz__warning_1').removeClass('req-text')
        }

        if ($('input[name="etf"]:checked').length == 0) {
            $('.quiz__warning_2').addClass('req-text')
        } else {
            $('.quiz__warning_2').removeClass('req-text')
        }
    }
})

$('input[name="types-assets"]').bind('change', function() {
    if ($('input[name="types-assets"]:checked').length > 0 && $('input[name="etf"]:checked').length > 0) {
        $('#next4').addClass('active')
    } else {
        $('#next4').removeClass('active')
    }
})


$('input[name="etf"]').bind('change', function() {
    if ($('input[name="types-assets"]:checked').length > 0 && $('input[name="etf"]:checked').length > 0) {
        $('#next4').addClass('active')
    } else {
        $('#next4').removeClass('active')
    }
})

$('#prev4').bind('click', function() {
    $('.quiz__card_4').fadeOut(1)
    $('.quiz__card_3').fadeIn(500)
    $('#step4').removeClass('active')
    $('#step3').removeClass('closed')
    $('#step3').addClass('active')
})


let clientSelect, clientName, descClient, birthday, pension,
    busyness, drawdowns, typeFond, typeInvest, timeInvest, riskCapital,
    riskFull, riskPercent, riskPriority, riskDrawdowns, riskFocus, classActives,
    removeActions, etf, strategy

let items = [],
    value, value2,
    removeSectors = []
let endWay = false

function calculte() {
    clientSelect = $('#clientSelect').val()
    clientName = $('#nameClient').val()
    descClient = $('#desc').val()
    birthday = $('#birthday').val()
    pension = $('#pension').val()
    busyness = $('#busyness').val()
    drawdowns = $('#drawdowns').val()
    timeInvest = $('#investHorizont').val()
    riskCapital = $("#startCapital").val()
    riskFull = $("#fullPortfolioCost").val()
    riskPercent = $(".risk__slider-field").val()
    riskPriority = $("#clientPriority").val()
    riskDrawdowns = $("#clientVolatility").val()
    riskFocus = $("input[name='focus-potfolio']:checked").val()
    items = []
    removeSectors = []

    var texts = [];

    $('.tag').each(function() {
        if ($(this).text()) texts.push($(this).text());
    });

    removeActions = texts.join(', ');
    var lastComma = removeActions.lastIndexOf(',');

    if ($('.tag').length == 1) {
        removeActions = $('.tag').text()
    } else {
        removeActions = removeActions.substring(0, lastComma) + ',' + removeActions.substring(lastComma + 1);

    }

    etf = $("input[name='etf']:checked").val()
    strategy = $("input[name='invest-strategy']:checked").val()
    $('input[name="types-assets"]:checked').each(function(_, e) {
        if ($(this).val() == '') {

        } else {
            value = $(this).val()
            items.push(value);
        }

    });


    $('input[name="sectors"]:checked').each(function() {
        value2 = $(this).val()
        removeSectors.push(value2);

    });

    if ($("#existingClient").prop('checked')) {
        $('#infoName').text('')
        $('#infoName').text(clientSelect)
    } else if ($("#newClient").prop('checked')) {
        $('#infoName').text('')
        $('#infoName').text(clientName)
        $('#infoDesc').text('')
        $('#infoDesc').text(descClient)
        $('#infoBirthday').text('')
        $('#infoBirthday').text(birthday)
        $('#infoPension').text('')
        $('#infoPension').text(pension)
        $('#infoBusyness').text('')
        $('#infoBusyness').text(busyness)
        $('#infoDrawdowns').text('')
        $('#infoDrawdowns').text(drawdowns)
    }
    $('#infoTimeInvest').text('')
    $("#infoTimeInvest").text(timeInvest)
    $('#infoStartCapital').text('')
    $("#infoStartCapital").text(riskCapital)
    // $('#infoFullCost').text('')
    // $("#infoFullCost").text(riskFull)
    $('#infoRiskPercent').text('')
    $("#infoRiskPercent").text(riskPercent)
    $('#infoInvestPriority').text('')
    $("#infoInvestPriority").text(riskPriority)
    // $('#infoDoDrawdowns').text('')
    // $("#infoDoDrawdowns").text(riskDrawdowns)
    $('#infoFocus').text('')
    $("#infoFocus").text(riskFocus)
    $('#infoActives').text('')
    $('#infoActives').text(items.join(', '))
    $('#infoRemoveSectors').text('')
    $('#infoRemoveSectors').text(removeSectors.join(', '))
    $('#infoRemoveActions').text('')
    $('#infoRemoveActions').text(removeActions)
    $('#infoEtf').text('')
    $('#infoEtf').text(etf)
    $('#infoStrategy').text('')
    $('#infoStrategy').text(strategy)
}

$('#next5').bind('click', function() {
    $('.quiz__card_5').fadeOut(1)
    $('.quiz__card_6').fadeIn(500)
    $('#step5').addClass('closed')
    $('#step6').addClass('active')

    calculte();
    endWay = true
})




$('#prev5').bind('click', function() {
    $('.quiz__card_5').fadeOut(1)
    $('.quiz__card_4').fadeIn(500)
    $('#step5').removeClass('active')
    $('#step4').removeClass('closed')
    $('#step4').addClass('active')
})

var urlView = "view.html";

$('#next6').bind('click', function() {
    $('#step6').addClass('closed')
    // calculte();
    $(".preloader").fadeIn(500)
    setTimeout(function() {
        $(location).attr('href', urlView);
    }, 4000);
})



$('#prev6').bind('click', function() {
    $('.quiz__card_6').fadeOut(1)
    $('.quiz__card_5').fadeIn(500)
    $('#step6').removeClass('active')
    $('#step5').removeClass('closed')
    $('#step5').addClass('active')
})



let backForth

let counterNav, numberStep

$('#change1').bind('click', function() {
    $(this).parents('.card').fadeOut(1)
    $('.quiz__card_1').fadeIn(500)
    $('.quiz-steps__item').removeClass('closed')
    $('.quiz-steps__item').removeClass('active')
    $('#step1').addClass('active')
    counterNav = "step-change"
    numberStep = 1
})


$('input[name="portfolio"]').bind('change', function() {
    if ($('#existingPortfolio').prop('checked')) {
        $(this).parents('.card').find('.quiz__right').fadeOut()
        $('.uploud-wrap').css('display', 'flex')
        $('.type-portfolio').fadeOut()

        if ($('.added-file').length > 0) {
            $('#next2').addClass('active')
        } else {
            $('#next2').removeClass('active')
        }
    } else if ($('#newPortfolio').prop('checked')) {
        $('.uploud-wrap').fadeOut(1)
        $('.type-portfolio').fadeIn()
        $(this).parents('.card').find('.quiz__right').fadeIn()
        if (!$('#investHorizont').val() == "") {
            if ($('#taxPortfolio').prop('checked')) {
                if (!$('#typeProfile').val() == "") {
                    $('#next2').addClass('active')
                } else if ($('#typeProfile').val() == "") {
                    $('#next2').removeClass('active')
                }
            } else if ($('#cofalifiedPortfolio').prop('checked')) {
                $('#next2').addClass('active')
            }
        } else if ($('#investHorizont').val() == "") {
            $('#next2').removeClass('active')
        }

    }
})


$('#change2').bind('click', function() {
    $(this).parents('.card').fadeOut(1)
    $('.quiz__card_2').fadeIn(500)
    $('.quiz-steps__item').removeClass('closed')
    $('.quiz-steps__item').removeClass('active')
    $('#step1').addClass('closed')
    $('#step2').addClass('active')
    counterNav = "step-change"
    numberStep = 2
})


$('#change3').bind('click', function() {
    $(this).parents('.card').fadeOut(1)
    $('.quiz__card_3').fadeIn(500)
    $('.quiz-steps__item').removeClass('closed')
    $('.quiz-steps__item').removeClass('active')
    $('#step1').addClass('closed')
    $('#step2').addClass('closed')
    $('#step3').addClass('active')
    counterNav = "step-change"
})

$('#change4').bind('click', function() {
    $(this).parents('.card').fadeOut(1)
    $('.quiz__card_4').fadeIn(500)
    $('.quiz-steps__item').removeClass('closed')
    $('.quiz-steps__item').removeClass('active')
    $('#step1').addClass('closed')
    $('#step2').addClass('closed')
    $('#step3').addClass('closed')
    $('#step4').addClass('active')
    counterNav = "step-change"
})


$('#change5').bind('click', function() {
    $(this).parents('.card').fadeOut(1)
    $('.quiz__card_5').fadeIn(500)
    $('.quiz-steps__item').removeClass('closed')
    $('.quiz-steps__item').removeClass('active')
    $('#step1').addClass('closed')
    $('#step2').addClass('closed')
    $('#step3').addClass('closed')
    $('#step4').addClass('closed')
    $('#step5').addClass('active')
    counterNav = "step-change"
})

$('.zoom__btn').bind('click', function() {
    $('.zoom__btn').removeClass('active')
    $(this).addClass('active')
})

$('.sorting-btn').bind('click', function() {
    $('.sorting-btn').removeClass('active')
    $(this).addClass('active')
})

$('.filters__dropdown-item').bind('click', function() {
    $('.navbar-bottom').addClass('flex-column')
    $('.navbar-bottom').removeClass('align-items-center')
    $('.navbar__card-settings').removeClass('ml-auto')
    $('.navbar__card-settings').css('margin-top', '7px')
    $('.filters-dropdown').addClass('ml-auto')
    $('.filters-main').css('display', 'flex')
    let top = $('.navbar').height()
    $('.cards-table').css('top', top + 30)
    if (cardToggler == 1) {
        $('.content').css('padding-top', top + 30 + 45)
    } else if (cardToggler == 0) {
        $('.content').css('padding-top', top + 30 + 25 + 63)
    }

})


$('.flters-list__item svg').bind('click', function() {
    $(this).parents('.flters-list__item').remove()
    if ($('.flters-list__item').length == 0) {
        $('.navbar-bottom').removeClass('flex-column')
        $('.navbar-bottom').addClass('align-items-center')
        $('.navbar__card-settings').addClass('ml-auto')
        $('.navbar__card-settings').css('margin-top', '0')
        $('.filters-dropdown').removeClass('ml-auto')
        $('.filters-main').fadeOut(1)
        let top = $('.navbar').height()
        if (cardToggler == 1) {
            $('.content').css('padding-top', top + 30 + 45)
        } else if (cardToggler == 0) {
            $('.content').css('padding-top', top + 30 + 25 + 63)
        }

        $('.cards-table').css('top', top + 30)
    }
})

let cardToggler = 1

$('.sorting-btn_2').bind('click', function() {
    $('.client-cards').fadeOut(1)
    $('.updated').fadeOut(1)
    $('.client-cards_stroke').fadeIn(1)
    $('.cards-table').fadeIn(1)

    let top = $('.navbar').height() + 30
    $('.cards-table').css('top', top)


    $('.content').css('padding-top', top + 62 + 25)

    cardToggler = 0
})

$('.sorting-btn_1').bind('click', function() {
    $('.client-cards').fadeIn(1)
    $('.updated').fadeIn(1)
    $('.client-cards_stroke').fadeOut(1)
    $('.cards-table').fadeOut(1)
    let top = $('.navbar').height() + 32 + 45
    $('.content').css('padding-top', top)

    cardToggler = 1
})

$('.filters-main__btn').bind('click', function() {
    $('.navbar-bottom').removeClass('flex-column')
    $('.navbar-bottom').addClass('align-items-center')
    $('.navbar__card-settings').addClass('ml-auto')
    $('.navbar__card-settings').css('margin-top', '0')
    $('.filters-dropdown').removeClass('ml-auto')
    $('.filters-main').fadeOut(1)
    let top = $('.navbar').height()
    if (cardToggler == 1) {
        $('.content').css('padding-top', top + 30 + 45)
    } else if (cardToggler == 0) {
        $('.content').css('padding-top', top + 30 + 25 + 63)
    }

    $('.cards-table').css('top', top + 30)
    $('.flters-list__item').remove()
})

$('.profit-graph__time-btn').bind('click', function() {
    $('.profit-graph__time-btn').removeClass('active')
    $(this).addClass('active')
})

$('.modal-notify-btn').bind('click', function() {
    setTimeout(function tick() {
        $('.signal-new').css('opacity', 1)
        $('.signal-new').slideDown(600)
    }, 200)

    setTimeout(function tick2() {
        $('.signal-new').css('background', '#fff')
    }, 1000)
})

$('.close-this').bind('click', function() {
    $('.signal-new').fadeOut(1)
})

$('.btn-login').bind('click', function() {
    $(this).addClass('loading')
    $('.login-incorrect').css('bottom', '6px')

})

$('.login-incorrect svg').bind('click', function() {
    $('.login-incorrect').css('bottom', '-65px')
})

$('.already-read').bind('click', function() {
    $(this).parents('.signal').removeClass('signal-new')
    $(this).parents('.signal').find('.badge.bg-danger').addClass('bg-gray')
    $(this).parents('.signal').find('.badge.bg-danger').text('Прочитанный')
    $(this).parents('.signal').find('.badge.bg-danger').removeClass('bg-danger')

})

$('.pay-offer').bind('click', function() {
    $(this).text('Портфель сохранен')
    $(this).addClass('disabled')
})

$('.save-draft').bind('click', function() {
    $(this).addClass('disabled')
})

$('.pay-offer-btn').bind('click', function() {
    $(this).text('Портфель сохранен')
    $(this).addClass('disabled')
})

$('.discard-changes').bind('click', function() {
    $(this).addClass('disabled')
})

$('#tabOverview').bind('click', function() {
    $('.export-txt').fadeOut(100)
})

$('#tabOverviewNotify').bind('click', function() {
    $('.export-txt').fadeIn(100)
})

$('.badge-edited').bind('click', function() {
    let textBadge = $(this).text()

    if (textBadge == 'Отслеживать') {
        $(this).removeClass('bg-success')
        $(this).addClass('bg-danger')
        $(this).text('Не уведомлять')
    } else if (textBadge == 'Не уведомлять') {
        $(this).addClass('bg-success')
        $(this).removeClass('bg-danger')
        $(this).text('Отслеживать')
    }
})

$('.sidebar-toggler').bind('click', function() {
    $('.sidebar-fixed').toggleClass('sidebar-open')
})

$(document).mouseup(function(e) { // событие клика по веб-документу
    var div = $(".sidebar-fixed"); // тут указываем ID элемента
    if (!div.is(e.target) // если клик был не по нашему блоку
        &&
        div.has(e.target).length === 0) { // и не по его дочерним элементам
        $('.sidebar-fixed').removeClass('sidebar-open')
    }
});

$(document).mouseup(function(e) { // событие клика по веб-документу
    var div = $("#changeNameField"); // тут указываем ID элемента
    if (!div.is(e.target) // если клик был не по нашему блоку
        &&
        div.has(e.target).length === 0) { // и не по его дочерним элементам
        $('#changeNameField').attr('contenteditable', 'false');
        $('#changeNameField').css('background', 'transparent');
    }
});

$('.edit').bind('click', function() {
    $('#changeNameField').attr('contenteditable', 'true');
    $('#changeNameField').css('background', '#f7f7f7');
})