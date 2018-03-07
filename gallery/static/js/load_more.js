// full ready web page
$(document).ready(function() {
    // create new socket
    socket = new WebSocket('ws://' + window.location.host + '/chat/');
    // this func call when websocket connect
    socket.onopen = function() {
        console.log('connect')
    }
    // this func call when websocket send message
    socket.onmessage = function(e) {
        // parse object
        data = JSON.parse(e.data)
        // get object from data
        for (num in data) {
            // obj = dict
            obj = data[num]
            // set new images
            $('div.images').append('<div class="col-md-4 image-add">' +
                '<div class="">' +
                '<img class="image-path image img-rounded" src="' + obj['path'] + '">' +
                '</div>' + '<div class="describe">' +
                '<div class="name"><strong>Tittle:</strong>' + obj['name'] + '</div>' +
                '<div class="time"><strong>Load:</strong>' + obj['datetime'] + '</div>' +
                '<div class="size"><strong>Size:</strong>' + obj['size'] + ' bytes</div>' +
                '</div>' +
                '</div>')
        }

    }
    // this func call when websocket close
    socket.onclose = function() {
        console.log('close')
    }
    // check ready state of socket
    if (socket.readyState == WebSocket.OPEN) {
        socket.onopen();
    }
    //  event form send message
    $('#load_more').click(function(event) {
        event.preventDefault();
        // send any message for receive signal
        text = JSON.stringify('more')
        socket.send(text)
    })
})
