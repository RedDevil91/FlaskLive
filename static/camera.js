var TIMER_SLEEP_TIME_MS = 100;
var stream_flag = false;
var timer;
var context = $("#stream_canvas").get(0).getContext("2d");


function get_image(){
    $.get("get_image/", function(img_data){
        var rawData = decode(img_data, {useTArray: true,
                                        colorTransform: false});
        var imgData = context.createImageData(480,360);
        imgData.data.set(rawData.data);
        context.putImageData(imgData, 0, 0, 0, 0, 480, 360);
    })
}

function start_stop_stream(){
    if (!stream_flag) {
//    TODO: if timer frequency is too high than it blocks the stop call! why?
        timer = setInterval(get_image, TIMER_SLEEP_TIME_MS);
        stream_flag = true;
    } else {
        clearInterval(timer);
        stream_flag = false;
    }
}

$("button").click(start_stop_stream);