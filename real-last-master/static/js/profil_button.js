const profil_button = document.getElementById('profil_button');
profil_button.addEventListener('click', () => {
  const input = document.getElementById('files');
  put_image(input.files[0]);
})