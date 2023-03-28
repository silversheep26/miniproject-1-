# miniproject-1-
항해 99 미니 프로젝트 


<!DOCTYPE html>
<html lang="en">

<head>
    <title>연진이</title>
    <style>
        html, body { overflow: hidden; }
        .video {
            height: 100%;
            width: 100%;
        }
    </style>
    <script>
      window.onload = function() {
        const video = document.getElementById("my-video");
        video.addEventListener('ended', function() {
          alert('동영상이 종료됩니다.');
          window.onbeforeunload = function() {
            return '이 페이지를 나가시겠습니까?';
          };
        });
      };
    </script>
</head>

<body>
    <div class="video">
        <iframe id="my-video" src="https://www.youtube.com/embed/l2_pbj39xC8?autoplay=1&loop=1" width="600" height="600" frameborder="0" allow="autoplay"></iframe>
    </div>
</body>

</html>
