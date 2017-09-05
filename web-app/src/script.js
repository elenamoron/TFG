(function (document) {
'use strict';
document.addEventListener('WebComponentsReady', function() {

    // We have to bind the template with the model
    var t = document.querySelector('#t');
    var ajaxRequest = t.$.dataAjax;

    // make the iron-ajax call
    t.postData = function() {
      ajaxRequest.body = {
        'text': t.dataToPost;
      } 
      ajaxRequest.generateRequest();
    }

    //callback on request complete
    t.postComplete = function(){
      alert('whoa! request complete');
    }
});
})(document);