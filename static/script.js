// As the dom loads
$(document).ready(function(){
$('button').click(function() {
	var pincode = $("#pincode").val();
	$.ajax({
			url: '/check',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
					console.log(response);
			},
			error: function(error) {
					console.log(error);
			}
	});
});
												
})

