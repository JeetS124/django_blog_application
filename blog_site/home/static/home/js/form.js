var password = document.getElementById("password")
    , confirm_password = document.getElementById("confirm_password");

function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

// password viewer
const showPassword = document.querySelector("#show-password");
const passwordField = document.querySelector("#password");

showPassword.addEventListener("click", function () {
    this.classList.toggle("fa-eye-slash");
    const type = passwordField.getAttribute("type")
        === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);
})

// password_Viewer_for_register_form
function password_show_hide() {
    var x = document.getElementById("password");
    var y = document.getElementById("confirm_password");
    var show_eye = document.getElementById("show_eye");
    var hide_eye = document.getElementById("hide_eye");
    hide_eye.classList.remove("d-none");
    if (x.type === "password") {
        x.type = "text";
        y.type = "text";
        show_eye.style.display = "none";
        hide_eye.style.display = "block";
    } else {
        x.type = "password";
        y.type = "password";
        show_eye.style.display = "block";
        hide_eye.style.display = "none";
    }
}

// password_Viewer_for_signin_form
function password_show_hide_signin() {
    var x = document.getElementById("password");
    var show_eye = document.getElementById("show_eye");
    var hide_eye = document.getElementById("hide_eye");
    hide_eye.classList.remove("d-none");
    if (x.type === "password") {
        x.type = "text";
        show_eye.style.display = "none";
        hide_eye.style.display = "block";
    } else {
        x.type = "password";
        show_eye.style.display = "block";
        hide_eye.style.display = "none";
    }
}

// for editor
// tinymce.init({
//     selector: "textarea#editor",
//     skin: 'bootstrap',
//     menubar: false,
//     plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed linkchecker a11ychecker tinymcespellchecker permanentpen powerpaste advtable advcode editimage tinycomments tableofcontents footnotes mergetags autocorrect typography inlinecss',
//     toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat',
//     // tinycomments_mode: 'embedded',
//     // tinycomments_author: 'Author name',
//     // mergetags_list: [
//     //     { value: 'First.Name', title: 'First Name' },
//     //     { value: 'Email', title: 'Email' },
//     // ]
//     setup: (editor) => {
//         // Apply the focus effect
//         editor.on("init", () => {
//             editor.getContainer().style.transition = "border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out";
//         });
//         editor.on("focus", () => {
//             (editor.getContainer().style.boxShadow = "0 0 0 .2rem rgba(0, 123, 255, .25)"),
//                 (editor.getContainer().style.borderColor = "#80bdff");
//         });
//         editor.on("blur", () => {
//             (editor.getContainer().style.boxShadow = ""),
//                 (editor.getContainer().style.borderColor = "");
//         });
//     },
// });




// // gdsgv
// tinymce.init({
//     selector: 'textarea#editor',
//     menubar: true,
//     statusbar: false,
//     plugins: 'autoresize anchor autolink charmap code codesample directionality fullpage help hr image imagetools insertdatetime link lists media nonbreaking pagebreak preview print searchreplace table template textpattern toc visualblocks visualchars',
//     toolbar: 'h1 h2 bold italic strikethrough blockquote bullist numlist backcolor | link image media | removeformat help fullscreen ',
//     skin: 'bootstrap',
//     toolbar_drawer: 'floating',
//     min_height: 200,
//     autoresize_bottom_margin: 16,
//     setup: (editor) => {
//         editor.on('init', () => {
//             editor.getContainer().style.transition = "border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out"
//         });
//         editor.on('focus', () => {
//             editor.getContainer().style.boxShadow = "0 0 0 .2rem rgba(0, 123, 255, .25)",
//                 editor.getContainer().style.borderColor = "#80bdff"
//         });
//         editor.on('blur', () => {
//             editor.getContainer().style.boxShadow = "",
//                 editor.getContainer().style.borderColor = ""
//         });
//     }
// });




// tinymce.init({
//     selector: '#editor',
//     height: 400,
//     plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed linkchecker a11ychecker tinymcespellchecker permanentpen powerpaste advtable advcode editimage tinycomments tableofcontents footnotes mergetags autocorrect typography inlinecss',
//     toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat',
// });