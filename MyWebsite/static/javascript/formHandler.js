$(function()
{
	// var successMsg = "Your message has been sent."; // Message shown on success.
	var failMsg = "Sorry it seems that you made a mistake in one of the fields above!"; // Message shown on fail.
var failMsg1 = "RRRR";
	var url = "";
	$("input,textarea").jqBootstrapValidation(
    {
     	preventSubmit: true,
     	submitSuccess: function($form, event)
	 	{
			if(!$form.attr('action')) // Check form doesnt have action attribute
			{
				event.preventDefault(); // prevent default submit behaviour
			
				var processorFile = "./includes/"+$form.attr('id')+".php";
				var formData = {};

				$form.find("input, textarea, option:selected").each(function(e) // Loop over form objects build data object
				{		
					var fieldData =  $(this).val();
					var fieldID =  $(this).attr('id');
				
					if($(this).is(':checkbox')) // Handle Checkboxes
					{
						fieldData = $(this).is(":checked");
					}
					else if($(this).is(':radio')) // Handle Radios
					{
						fieldData = $(this).val()+' = '+$(this).is(":checked");
					}
					else if($(this).is('option:selected')) // Handle Option Selects
					{
						fieldID = $(this).parent().attr('id');
					}
					formData[fieldID] = fieldData;		
				});
				if(formData['select_2176']=="0") // recruiting
				{
failMsg1="SSSS";
					processorFile = "../_complogin.php";
					url = "../tnp/company/compindex.php";
				}
				else // training
				{
					processorFile = "../_complogin2.php";
					url = "../tnp/training/company/compindex.php";
				}
				document.getElementById("comp-login-btn").disabled = true;
 	   			document.getElementById("comp-login-btn").innerHTML = "Please wait...";
				$.ajax({
		        	url: processorFile,
		    		type: "POST",
		    		data: formData,
		    		cache: false,
		    		success: function(result,status,xhr) // Success
		 			{  
						// $form.append("<div id='form-alert'><div class='alert alert-success'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>"+successMsg+"</strong></div></div>");		
		 	   			if(result=="Login Successfull"){
			 	   			window.location = url;
			 	   		}
			 	   		else{
			 	   			document.getElementById("comp-login-btn").disabled = false;
 	   						document.getElementById("comp-login-btn").innerHTML = "Login";

							$form.append("<div id='form-alert'><div class='alert alert-danger'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>"+result+"</strong></div></div>");	
			 	   		}
		 	   		},
			   		error: function() // Fail
			   		{
						document.getElementById("comp-login-btn").disabled = false;
	 	   				document.getElementById("comp-login-btn").innerHTML = "Login";
						$form.append("<div id='form-alert'><div class='alert alert-danger'><button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button><strong>"+failMsg+failMsg1+"</strong></div></div>");	
			   		},
					complete: function() // Clear
					{
						$form.trigger("reset");
					},
		   		});
			}
         },
         filter: function() // Handle hidden form elements
		 {
			 return $(this).is(":visible");
         },
	 });
});
