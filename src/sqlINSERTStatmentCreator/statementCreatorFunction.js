function createINSERT(){
	
	var inputVal = document.getElementById("inputQuery").value;

	if(inputVal == ""){
		inputVal = "worlds largest hamburger"
	}
	
	var settings = {
	  "url": "https://api.bing.microsoft.com/v7.0/search?q=worlds largest hamburger&count=30",
	  "method": "GET",
	  "timeout": 0,
	  "headers": {
		"Ocp-Apim-Subscription-Key": "68b83e74bbac4643a7299411e9ba88d2"
	  },
	};

	$.ajax(settings).done(function (response) {
	  console.log(response);
	});
}