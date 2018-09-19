var TIMER_SLEEP_TIME_MS = 100;
var stream_flag = false;
var timer;

function get_image(data){
    $.get("get_image/", function(data){
        $("#test").attr("src", "data:image/png;base64," + data);
    })
}

function start_stop_stream(){
    console.log("PUSHED!");
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