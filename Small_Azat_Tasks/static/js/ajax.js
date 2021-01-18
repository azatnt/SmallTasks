$(document).on('submit', '.com-form', function(event){
			event.preventDefault();
			console.log($(this).serialize());
			$.ajax({
				type: 'POST',
				url: $(this).attr('action'),
				data: $(this).serialize(),
				dataType: 'json',
				success: function(response) {
					$('.main-comment-section').html(response['form']);
					// $('.comment_form').fadeIn()


					// $('textarea').val('');
					// $('.reply-btn').click(function(event) {
					// 	event.preventDefault;
					// 	$(this).parent().parent().next('.replied-comments').fadeIn();
					// });
				},
				error: function(rs, e) {
					console.log(rs.responseText);
				},
			});
		});