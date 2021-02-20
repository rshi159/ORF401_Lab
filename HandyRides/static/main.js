
function getCookie(c_name) {
   var i,x,y,ARRcookies=document.cookie.split(";");
   for (i=0;i<ARRcookies.length;i++){
      x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
      y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
      x=x.replace(/^\s+|\s+$/g,"");
      if (x==c_name) {
        return unescape(y);
      }
   }
}
function setCookie(c_name,value,exdays) {
   var exdate=new Date();
   exdate.setDate(exdate.getDate() + exdays);
   var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
   document.cookie=c_name + "=" + c_value;
}

// checks if user visited page before. if not, set cookie
// and redirect to splash page
function checkCookie(c_name, value, exdays) {
   if(getCookie(c_name) == null){
      console.log("New Visitor");
      setCookie(c_name, value, exdays);
      console.log("Saved cookie. Redirecting...");
      window.location.replace("http://127.0.0.1:8000/");
   }
   console.log("exited check cookie function");
}

function checkForm(form){
   var search_city = form.children[1].value;
   var search_state = form.children[3].value;
   console.log(search_city);
   console.log(search_state);

   var elon = "elon musk";

   if(search_city.toLowerCase().includes(elon))
      alert("He's not here!!!");

   // //https://stackoverflow.com/questions/10232366/how-to-check-if-a-variable-is-null-or-empty-string-or-all-whitespace-in-javascri
   if (search_city == null | search_city.match(/^ *$/) !== null)
   {
      console.log("no input in search city");
      return false;
   }
   if (search_state == null | search_state.match(/^ *$/) !== null)
   {
      console.log("no input in search state");
      return false;
   }

   return true;
}