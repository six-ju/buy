const putFile = file => {
  const albumBucketName = 'minprojectbuy'; // S3의 버킷 이름
  const region = 'ap-northeast-2'; // 서울
  const accessKeyId = 'AKIA5MALC7S46ZH65COI'; // IAM에서 생성한 사용자의 accessKeyId
  const secretAccessKey = 'VuW8hw/5MX1itDweoT2JwrpRjYQugudC0e/Ii4rd'; // IAM에서 생성한 사용자의 secretAccessKey
  const profil_key = file.name
  AWS.config.update({
    region,
    accessKeyId,
    secretAccessKey
  });
  const upload = new AWS.S3.ManagedUpload({
    params: {
      Bucket: albumBucketName,
      Key: file.name,
      Body: file,
      ACL: "public-read"
    }
  });

  const promise = upload.promise();
  promise.then(
    function(data) {
      console.log("Successfully uploaded photo.");
    },
    function(err) {
      return console.log("There was an error uploading your photo: ", err.message);
    }
  );
  const download_upload_files = 'https://'+albumBucketName+'.s3.'+region+'.amazonaws.com/'+profil_key
  $.ajax({
    type: 'POST',
    url: '/upload',
    data: {download_upload_files_give:download_upload_files},
    success: function (response) {
        alert(response['msg'])
        window.location.reload()
    }
  })
};
