function submit_message(event) {
    event.preventDefault();

    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var posturl = document.getElementById("posturl");
    var downloadpfp = document.getElementById("downloadpfp");

    var entry = {
        email: email.value,
        password: password.value,
        posturl: posturl.value,
        downloadpfp: downloadpfp.value
    };

    fetch(`http://127.0.0.1:5000/api`, {
        method: "POST",
        // credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      })
      .then(function(response) {
        if (response.status !== 200) {
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          return;
        }
        response.blob().then(blob => {
        const url = URL.createObjectURL(blob)
        document.location = url
        });
      })
      .catch(function(error) {
        console.log("Fetch error: " + error);
    });
}

// $(document).ready(function() {
//     $('form').on('submit', function(event) {
//     console.log($('#email').val(), $('#password').val(), $('#posturl').val(), $('#downloadpfp').val())

//     var entry = 
//         {
//             email : $('#email').val(),
//             password: $('#password').val(),
//             posturl: $('#posturl').val(),
//             downloadpfp: $('#downloadpfp').val()
//         }

//         console.log(entry)

//     $.ajax({
//         data : entry,
//             type : 'POST',
//             url : 'http://127.0.0.1:5000/api'
//             })
//         .done(function(data) {
//     console.log("DONE")
//             console.log(data);
//         //     data.blob()
//         // blob => {
//             var binaryData = [];
//         binaryData.push(data);
//         const url = window.URL.createObjectURL(new Blob(binaryData, {type: "application/zip"}))
//         // const url = URL.createObjectURL(data)
//         document.location = url
//     });
//     event.preventDefault();
//     });
// });