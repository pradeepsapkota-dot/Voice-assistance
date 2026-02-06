$(document).ready(function () {
    // Textillate initialization
 $('.text').textillate({
    loop: true,
    sync: true,
    in: { 
        effect: 'bounceIn',
        sync: true,
    },
    out: { 
        effect: 'bounceOut',
        sync: true 
    }
    
});
    //Mic button Tigger
    $("#MicBtn").click(function () { 
        eel.playassisound();
        $("#Circular" ).attr("hidden", true);
        $("#LuffyWave" ).attr("hidden", false);
        eel.allcommands()

        
    });


    //Luffy Wave
        $('.luffy-message').textillate({
        loop: true,
        sync: true,
        in: { effect: 'fadeInUp', sync: true },
        out: { effect: 'fadeOutUp', sync: true }
    });

        function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'l' && (e.ctrlKey || e.metaKey)) //Ctrl + l to open mic
            {
            eel.playassisound()
            $("#Circular").attr("hidden", true);
            $("#LuffyWave").attr("hidden", false);
            eel.allcommands()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message) {

        if (message!="") {

        $("#Circular").attr("hidden", true);
        $("#LuffyWave").attr("hidden", false);
        eel.allcommands(message)
        $('#chatbox').val('');
        $('#chatbox').attr('hidden', false);
        $('#SendBtn').attr('hidden', true);
    }
    }

    function ShowSendButton(message) {

        if (message.length == 0) {
            $('#MicBtn').attr('hidden', false);
            $('#SendBtn').attr('hidden', true);
        }
        else {
            $('#MicBtn').attr('hidden', true);
            $('#SendBtn').attr('hidden', false);
        }
    }   

    $('#chatbox').keyup(function () {
        let message = $('#chatbox').val();
        ShowSendButton(message);
    });

    $('#SendBtn').click(function () {
        let message = $('#chatbox').val();
        PlayAssistant(message);
    });

    $('#chatbox').keypress(function (e) {
        key = e.which;
        if (key == 13)  // the enter key code
        {
            let message = $('#chatbox').val();
            PlayAssistant(message);
        }
    });

});
