var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
var csrftoken = "";
var KK;
KindEditor.ready(function(K){
     KK = K;
});
function searchtoken() {
    console.log("sdf");
    if (csrfitems.length > 0) {
        csrftoken = csrfitems[0].value;
        clearInterval(_interval);
        console.log("csrftoken:" + csrftoken);
        window.editor = KK.create('#id_content',{
            uploadJson: '/kin/uploadImg/',
            extraFileUploadParams: {
                    csrfmiddlewaretoken:csrftoken
                },
            // 指定大小
            width:'800px',
            height:'400px',
        });
    }
}
_interval = setInterval(searchtoken, 500);
