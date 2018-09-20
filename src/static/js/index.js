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
					html +=("<div id='box' class='col-md-4'><div class='thumbnail'><div class='rounded float-left'style='width:100;height:80px;text-align:center;'><a href='"+detail+"'><h3>"
					+response[i].model__model+"<br>"+response[i].car__count+"</h3></a></div></div></div>");
					}
				$('#model-list').html(html);
				$('#model-list').click(function(){
					$(this).hide();
				});	
			}
		});
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

	// ================================================================================
	// To check if modal inputs satisfy the conditions and enable search button | ends
	// ================================================================================

	$(window).on('scroll', fixHeader);
		var header = $('nav');
		var headerOffset = header.offset().top;
		function fixHeader(evt){

		var currentScroll = $(window).scrollTop()
		if(headerOffset <= currentScroll){
			header.addClass('navbar-fixed-top').css({"right":"10px","left":"10px"});
		}
		else{
			 header.removeClass('navbar-fixed-top')
		}
	}


	// =========================finance-container animation ========================
	$("#why-finance-with-us-btn > p,#key-finance-features-btn > p, #get-pre-qualified-btn > p").slideUp();

	$("#btn1").click(function(){
		$("#why-finance-with-us-btn > p").slideToggle();
	});

	$("#btn2").click(function(){
		$("#key-finance-features-btn > p").slideToggle();
	});

	$("#btn3").click(function(){
		$("#get-pre-qualified-btn > p").slideToggle();
	});

	// =========================finance-container animation ends====================


	// =============buy or sell container==============

	$("#selling").hide();
	$('#selling-btn').on("click",function(e){
		e.preventDefault();
		$("#selling").show() && $("#buying").hide();
		$('#buying-btn').on("click",function(){	
			$("#buying").show() && $("#selling").hide();		
		});
	});

	$("#list-img-car-list img").click(function(){
		
		var thumbnailSrc = $(this).attr('src');
		$(this).parents("#img-bx").find("#list-img img").attr("src",thumbnailSrc);

	});
	
	// ========================Blinking headings====================================
	
	function pulse(){
		$(".blink").fadeOut('slow');
		$(".blink").fadeIn('slow');
		
	}
	setInterval(pulse,1000);	

});
