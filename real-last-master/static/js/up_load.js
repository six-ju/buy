let today = new Date();
let year = today.getFullYear(); // 년도
let month = today.getMonth() + 1;
let date = today.getDate();
let hours = today.getHours(); // 시
let minutes = today.getMinutes();  // 분
let seconds = today.getSeconds();  // 초
now_date = (year+'-'+month+'-'+date+'-'+hours+'-'+minutes+'-'+seconds)
function upload_button() {
    let title = $('#title').val()
    let category = $('#category').val()
    let start_price = $('#start_price').val()
    let date = now_date
    let content = $('#content').val()
    if ($("#title").val().length == 0) {
        alert("제목은 필수입니다");

        $("#title").focus();
        return false;
    }
    if ($("#category").val().length == 0 ||$("#category").val() == 'none') {
        alert("카테고리 골라주세요");
        $("#category").focus();
        return false;
    }
    if ($("#start_price").val().length == 0 || $("#start_price").val() == "0") {
        alert("시작 금액을 정해주세요");
        $("#start_price").focus();
        return false;
    }
    if ($("#content").val().length == 0) {
        alert("내용을 써주세요");
        $("#content").focus();
        return false;
    }
    const input = document.getElementById('upload_file');
    let file = input.files[0]
    let download_upload_files = 'https://minprojectbuy.s3.ap-northeast-2.amazonaws.com/'+file.name

    $.ajax({
        type: 'POST',
        url: '/upload',
        data: {title_give: title,category_give: category,
            start_price_give: start_price,date_give: date, content_give: content
        , files_give :download_upload_files},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    })
}
