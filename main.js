console.log("Hello");
 var socket = io.connect(location.protocol +'//' + document.domain + ':' + location.port);
//     socket.on('connect', function() {
//         socket.emit('my event', {data: 'I\'m connected!'});
//     });
socket.on('push',function(data){
	console.log(data)
})
function send()
{
	var inputBox =document.getElementById('inputBox');
	socket.emit('message',inputBox.value)
	inputBox.value="";
}
function getUsers()
{
	//console.log('Clicked')
	fetch('/users').then(function(res){res.json().then(function(data){
		console.log(data)
	})})//provide full path for google//js is non-blocking//
}