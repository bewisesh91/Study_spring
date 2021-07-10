$(document).ready(function () {
    $('#cards-box').html("");
    listing();
});

function openClose() {
    let status = $('#posting-box').css('display')
    if (status == 'block') {
        $('#posting-box').hide()
        $('#posting-box-btn').text('포스팅 박스 열기')
    } else {
        $('#posting-box').show()
        $('#posting-box-btn').text('포스팅 박스 닫기')
    }
}

function posting() {
    let url = $('#posting-url').val();
    let comment = $('#posting-comment').val();
    console.log(url, comment)

    $.ajax({
        type: "POST",
        url: "/memo",
        data: { url_give: url, url_comment_give: comment},
        success: function (response) { // 성공하면
            if (response["result"] == "success") {
                alert("포스팅 완료");
                window.location.reload();
            } else {
                alert("서버 오류")
            }
        }
    })
}

function listing() {
    $.ajax({
        type: "GET",
        url: "/memo",
        data: {},
        success: function (response) {
            console.log(response)
            let urlDatas = response["urlDatas"];
            for (let i = 0; i < urlDatas.length; i++) {
                post(urlDatas[i]["image"], urlDatas[i]["url"], urlDatas[i]["title"], urlDatas[i]["description"], urlDatas[i]["url_comment"])
            }
        }
    })
}

function post(image, url, title, description, url_comment) {
    let temp_html = `<div class="card">
                        <img class="card-img-top"
                            src="${image}"
                            alt="Card image cap">
                        <div class="card-body">
                            <a href="${url}" target="_blank" class="card-title">
                                <h5 class="card-title"> ${title} </h5>
                            </a>
                            <p class="card-text"> ${description} </p>
                            <p class="card-text card-comment"> ${url_comment} </p>
                        </div>
                    </div>`;
    $("#cards-box").append(temp_html);
}
