$(document).ready(function(){
	$('select[name="make"]').change(function(){
		var $select_model = $('select[name="model"]');
		var make_val= $(this).val();
		var group_selection = $('option:selected', this).text();
		
		if (make_val === 'select'){
			$('option,optgroup',$select_model).show();
		}
		else{
			$('optgroup, optgroup > option',$select_model).hide();
			$('optgroup[label="'+group_selection+'"]',$select_model).children().addBack().show();
		}
	});

	// ========================================================
	// This Ajax call will display selected car models | Starts
	// ========================================================
	$("#make > li > a").click(function(event){
		$('#model-list').show();
		event.stopPropagation();
		event.preventDefault();
		var myurl = $(this).attr('href');
		console.log(myurl);

		$.ajax({
			url:myurl,
			success:function(response){
				console.log(response);
				console.log(response[0].car__count);
				


				var html='';
				for (i=0;i<response.length;i++){
					var detail= 'http://127.0.0.1:8000/mycar/models_detail/'+response[i].model__id;
					html +=("<div id='box' class='col-md-4'><div class='thumbnail'><div class='rounded float-left'style='width:100;height:100px;text-align:center;'><a href='"+detail+"'><h3>"
					+response[i].model__model+"<br>"+response[i].car__count+"</h3></a></div></div></div>");

					}
				$('#model-list').html(html);
				$('#model-list').click(function(){
					$(this).hide();
				});	
			}
		});
	});
	// ========================================================
	// This Ajax call will display selected car models | Ends
	// ========================================================
	
	// ==================================
	// slide in as we scroll down | start
	// ==================================
	$('.mama').not(':eq(0)').css('opacity',0);
	$(window).scroll(function(){
		var windowHeight = $(window).height();
		var windowScrollPosTop = $(window).scrollTop();
		var windowScrollPosBottom = windowHeight + windowScrollPosTop;
		
		var objectOffset = $('.mama').offset();
		var objectOffsetTop = objectOffset.top;

		$('.status').html(objectOffsetTop);
		if (!$('.mama').hasClass('animation-complete')){
			if (windowScrollPosBottom > objectOffsetTop){
				$('.mama').animate({'opacity':1},
				3000).addClass('animation-complete');
			}		
		}
		
	});

	// ================================================================================
	// To check if modal inputs satisfy the conditions and enable search button | start
	// ================================================================================
	$("#modal-search-btn").attr("disabled",true);
	$("#id_minprice,#id_maxprice").keyup(function(){
		$("#id_minprice,#id_maxprice").each(function(){
		if($(this).val().length !=0){
			$("#modal-search-btn").attr("disabled",false);
			}
		else{
			$("#modal-search-btn").attr("disabled",true);
			}
		});
	});

});
