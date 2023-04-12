function reset_check_oclusal(){
    const img_ausente = window.document.getElementById('img_oclusal_ausente');
    var chk_ausente = window.document.getElementById("chk_oclusal_ausente");
    if(chk_ausente.checked == true){
        chk_ausente.checked = false;
        console.log('oclusal_ausente: ' + chk_ausente.checked);
    };
    img_ausente.style.border = '2px solid black'
    img_ausente.style.position = 'none';
    img_ausente.style.bottom = '0';
    img_ausente.style.opacity = 0.5;

    const img_doenca_periodontal = window.document.getElementById('img_oclusal_doenca_periodontal');
    var chk_doenca_periodontal = window.document.getElementById("chk_oclusal_doenca_periodontal");
    if(chk_doenca_periodontal.checked == true){
        chk_doenca_periodontal.checked = false;
        console.log('oclusal_doenca_periodontal: ' + chk_doenca_periodontal.checked);
    };
    img_doenca_periodontal.style.border = '2px solid black'
    img_doenca_periodontal.style.position = 'none';
    img_doenca_periodontal.style.bottom = '0';
    img_doenca_periodontal.style.opacity = 0.5;

    const img_faceta_degaste = window.document.getElementById('img_oclusal_faceta_degaste');
    var chk_faceta_degaste = window.document.getElementById("chk_oclusal_faceta_degaste");
    if(chk_faceta_degaste.checked == true){
        chk_faceta_degaste.checked = false;
        console.log('oclusal_faceta_degaste: ' + chk_faceta_degaste.checked);
    };
    img_faceta_degaste.style.border = '2px solid black'
    img_faceta_degaste.style.position = 'none';
    img_faceta_degaste.style.bottom = '0';
    img_faceta_degaste.style.opacity = 0.5;

    
    const img_fratura = window.document.getElementById('img_oclusal_fratura');
    var chk_fratura = window.document.getElementById("chk_oclusal_fratura");
    if(chk_fratura.checked == true){
        chk_fratura.checked = false;
        console.log('oclusal_fratura: ' + chk_fratura.checked);
    };
    img_fratura.style.border = '2px solid black'
    img_fratura.style.position = 'none';
    img_fratura.style.bottom = '0';
    img_fratura.style.opacity = 0.5;

    const img_selante_fazer = window.document.getElementById('img_oclusal_selante_fazer');
    var chk_selante_fazer = window.document.getElementById("chk_oclusal_selante_fazer");
    if(chk_selante_fazer.checked == true){
        chk_selante_fazer.checked = false;
        console.log('oclusal_selante_fazer: ' + chk_selante_fazer.checked);
    };
    img_selante_fazer.style.border = '2px solid black'
    img_selante_fazer.style.position = 'none';
    img_selante_fazer.style.bottom = '0';
    img_selante_fazer.style.opacity = 0.5;
}


function oclusal(){
    reset_check_oclusal();
    const a = window.document.getElementById('distal');
    const b = window.document.getElementById('oclusal');
    const c = window.document.getElementById('lingual');
    const d = window.document.getElementById('mesial');
    const e = window.document.getElementById('vestibular');

    const f = window.document.getElementById('display_oclusal');
    const g = window.document.getElementById('display_distal');
    f.style.display = 'flex';
    g.style.display = 'none';

    f.style.border = '2px solid black';
    f.style.marginBottom = '200px';
    f.style.marginTop = '200px';
    g.style.border = 'none';
   


    a.style.background = 'rgb(255, 255, 255)';
    a.style.boxShadow = 'none';

    b.style.background = 'rgb(35,167,240)';
    b.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    c.style.background = 'rgb(255, 255, 255)';
    c.style.boxShadow = 'none';

    d.style.background = '#ffffff';
    d.style.boxShadow = 'none';

    e.style.background = '#ffffff';
    e.style.boxShadow = 'none';

}

function chk_oclusal_ausente(){
    const b = window.document.getElementById("chk_oclusal_ausente");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_oclusal_ausente');
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('oclusal_ausente: '+b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('oclusal_ausente: '+b.checked);
    }
}
function chk_oclusal_doenca_periodontal(){
    const a = window.document.getElementById('img_oclusal_doenca_periodontal');
    const b = window.document.getElementById("chk_oclusal_doenca_periodontal");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('oclusal_doenca_periodontal: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('distal_doenca_periodontal: ' + b.checked);
    }
}
function chk_distal_faceta_desgate(){
    const a = window.document.getElementById('img_distal_faceta_degaste');
    const b = window.document.getElementById("chk_distal_faceta_degaste");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_faceta_degaste: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('distal_faceta_degaste: ' + b.checked);
    }
}
function chk_distal_fratura(){
    const a = window.document.getElementById('img_distal_fratura');
    const b = window.document.getElementById("chk_distal_fratura");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_fratura: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('distal_fratura: ' + b.checked);
    }
}
function chk_distal_selante_fazer(){
    const a = window.document.getElementById('img_distal_selante_fazer');
    const b = window.document.getElementById("chk_distal_selante_fazer");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_selante_fazer: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('distal_selante_fazer: ' + b.checked);
    }
}
function chk_distal_selante_satisfatorio(){
    const a = window.document.getElementById('img_distal_selante_satisfatorio');
    const b = window.document.getElementById("chk_distal_selante_satisfatorio");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_selante_satisfatorio: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('distal_selante_satisfatorio: ' + b.checked);
    }
}
function checar7(){
    const a = window.document.getElementById('img_anomalia_de_forma');
    const b = window.document.getElementById("chk_anomalia_de_forma");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('anomalia_de_forma: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('anomalia_de_forma: ' + b.checked);
    }
}
function checar8(){
    const a = window.document.getElementById('img_defeito_de_esmalte');
    const b = window.document.getElementById("chk_defeito_de_esmalte");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('defeito_de_esmalte: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('defeito_de_esmalte: ' + b.checked);
    }
}
function checar9(){
    const a = window.document.getElementById('img_supranumerario');
    const b = window.document.getElementById("chk_supranumerario");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('supranumerario: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('supranumerario: ' + b.checked);
    }
}
function checar10(){
    const a = window.document.getElementById('img_restauracao_protese_concluida');
    const b = window.document.getElementById("chk_restauracao_protese_concluida");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('restauracao_protese_concluida: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('restauracao_protese_concluida: ' + b.checked);
    }
}
function checar11(){
    const a = window.document.getElementById('img_tratamento_endondontico_concluido');
    const b = window.document.getElementById("chk_tratamento_endondontico_concluido");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('tratamento_endondontico_concluido: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('tratamento_endondontico_concluido: ' + b.checked);
    }
}
function checar12(){
    const a = window.document.getElementById('img_calculo_recessao_gengival');
    const b = window.document.getElementById("chk_calculo_recessao_gengival");
    b.checked = !b.checked;
    if(b.checked == true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = 1;
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('calculo_recessao_gengival: ' + b.checked);
    }
    else if (b.checked == false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = 0.5;
        console.log('calculo_recessao_gengival: ' + b.checked);
    }
}