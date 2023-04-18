
function reset_check_distal(){
    const img_higido = window.document.getElementById('img_distal_higido');
    const chk_higido = window.document.getElementById("chk_distal_higido");
    if(chk_higido.checked === true){
        chk_higido.checked = false;
        console.log('reset-distal_higido: ' + chk_higido.checked);
    }
    img_higido.style.border = '2px solid black'
    img_higido.style.position = 'none';
    img_higido.style.bottom = '0';
    img_higido.style.opacity = '0.5';
    img_higido.style.boxShadow = 'none';

    const img_mancha_branca_ativa = window.document.getElementById('img_distal_mancha_branca_ativa');
    const chk_mancha_branca_ativa = window.document.getElementById("chk_distal_mancha_branca_ativa");
    if(chk_mancha_branca_ativa.checked === true){
        chk_mancha_branca_ativa.checked = false;
        console.log('reset-distal_mancha_branca_ativa: ' + chk_mancha_branca_ativa.checked);
    }
    img_mancha_branca_ativa.style.border = '2px solid black'
    img_mancha_branca_ativa.style.position = 'none';
    img_mancha_branca_ativa.style.bottom = '0';
    img_mancha_branca_ativa.style.opacity = '0.5';
    img_mancha_branca_ativa.style.boxShadow = 'none';

    const img_distal_lesao_carie_primaria = window.document.getElementById('img_distal_lesao_carie_primaria');
    const chk_distal_lesao_carie_primaria = window.document.getElementById("chk_distal_lesao_carie_primaria");
    if(chk_distal_lesao_carie_primaria.checked === true){
        chk_distal_lesao_carie_primaria.checked = false;
        console.log('reset-distal_lesao_carie_primaria: ' + chk_distal_lesao_carie_primaria.checked);
    }
    img_distal_lesao_carie_primaria.style.border = '2px solid black'
    img_distal_lesao_carie_primaria.style.position = 'none';
    img_distal_lesao_carie_primaria.style.bottom = '0';
    img_distal_lesao_carie_primaria.style.opacity = '0.5';
    img_distal_lesao_carie_primaria.style.boxShadow = 'none';

    const img_distal_lesao_carie_cronica = window.document.getElementById('img_distal_lesao_carie_cronica');
    const chk_distal_lesao_carie_cronica = window.document.getElementById("chk_distal_lesao_carie_cronica");
    if(chk_distal_lesao_carie_cronica.checked === true){
        chk_distal_lesao_carie_cronica.checked = false;
        console.log('reset-distal_lesao_carie_cronica: ' + chk_distal_lesao_carie_cronica.checked);
    }
    img_distal_lesao_carie_cronica.style.border = '2px solid black'
    img_distal_lesao_carie_cronica.style.position = 'none';
    img_distal_lesao_carie_cronica.style.bottom = '0';
    img_distal_lesao_carie_cronica.style.opacity = '0.5';
    img_distal_lesao_carie_cronica.style.boxShadow = 'none';

    const img_mancha_inativa = window.document.getElementById('img_distal_mancha_inativa');
    const chk_mancha_inativa = window.document.getElementById("chk_distal_mancha_inativa");
    if(chk_mancha_inativa.checked === true){
        chk_mancha_inativa.checked = false;
        console.log('reset-distal_mancha_inativa: ' + chk_mancha_inativa.checked);
    }
    img_mancha_inativa.style.border = '2px solid black'
    img_mancha_inativa.style.position = 'none';
    img_mancha_inativa.style.bottom = '0';
    img_mancha_inativa.style.opacity = '0.5';
    img_mancha_inativa.style.boxShadow = 'none';

    const img_ausente = window.document.getElementById('img_distal_ausente');
    const chk_ausente = window.document.getElementById("chk_distal_ausente");
    if(chk_ausente.checked === true){
        chk_ausente.checked = false;
        console.log('reset-distal_ausente: ' + chk_ausente.checked);
    }
    img_ausente.style.border = '2px solid black'
    img_ausente.style.position = 'none';
    img_ausente.style.bottom = '0';
    img_ausente.style.opacity = '0.5';

    const img_doenca_periodontal = window.document.getElementById('img_distal_doenca_periodontal');
    const chk_doenca_periodontal = window.document.getElementById("chk_distal_doenca_periodontal");
    if(chk_doenca_periodontal.checked === true){
        chk_doenca_periodontal.checked = false;
        console.log('reset-distal_doenca_periodontal: ' + chk_doenca_periodontal.checked);
    }
    img_doenca_periodontal.style.border = '2px solid black'
    img_doenca_periodontal.style.position = 'none';
    img_doenca_periodontal.style.bottom = '0';
    img_doenca_periodontal.style.opacity = '0.5';

    const img_faceta_degaste = window.document.getElementById('img_distal_faceta_degaste');
    const chk_faceta_degaste = window.document.getElementById("chk_distal_faceta_degaste");
    if(chk_faceta_degaste.checked === true){
        chk_faceta_degaste.checked = false;
        console.log('reset-distal_faceta_degaste: ' + chk_faceta_degaste.checked);
    }
    img_faceta_degaste.style.border = '2px solid black'
    img_faceta_degaste.style.position = 'none';
    img_faceta_degaste.style.bottom = '0';
    img_faceta_degaste.style.opacity = '0.5';


    const img_fratura = window.document.getElementById('img_distal_fratura');
    const chk_fratura = window.document.getElementById("chk_distal_fratura");
    if(chk_fratura.checked === true){
        chk_fratura.checked = false;
        console.log('reset-distal_fratura: ' + chk_fratura.checked);
    }
    img_fratura.style.border = '2px solid black'
    img_fratura.style.position = 'none';
    img_fratura.style.bottom = '0';
    img_fratura.style.opacity = '0.5';

    const img_selante_fazer = window.document.getElementById('img_distal_selante_fazer');
    const chk_selante_fazer = window.document.getElementById("chk_distal_selante_fazer");
    if(chk_selante_fazer.checked === true){
        chk_selante_fazer.checked = false;
        console.log('reset-distal_selante_fazer: ' + chk_selante_fazer.checked);
    }
    img_selante_fazer.style.border = '2px solid black'
    img_selante_fazer.style.position = 'none';
    img_selante_fazer.style.bottom = '0';
    img_selante_fazer.style.opacity = '0.5';
}


function btn_distal(){
    // reset_check_distal();
    const btn_distal = window.document.getElementById('distal');
    const btn_oclusal = window.document.getElementById('oclusal');
    const btn_lingual = window.document.getElementById('lingual');
    const btn_mesial = window.document.getElementById('mesial');
    const btn_vestibular = window.document.getElementById('vestibular');

    const display_distal = window.document.getElementById('display_distal');
    // display_distal.style.marginBottom = '200px';
    // display_distal.style.marginTop = '200px';
    display_distal.style.display = 'flex';
    const display_oclusal = window.document.getElementById('display_oclusal');
    const display_mesial = window.document.getElementById('display_mesial');
    display_oclusal.style.border = 'none';
    display_oclusal.style.display = 'none';
    display_mesial.style.display = 'none';


    btn_distal.style.background = 'rgb(35,167,240)';
    btn_distal.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';

    btn_oclusal.style.background = '#ffffff';
    btn_oclusal.style.boxShadow = 'none';

    btn_lingual.style.background = '#ffffff';
    btn_lingual.style.boxShadow = 'none';

    btn_mesial.style.background = '#ffffff';
    btn_mesial.style.boxShadow = 'none';

    btn_vestibular.style.background = '#ffffff';
    btn_vestibular.style.boxShadow = 'none';

}
function chk_distal_higido(){
    const b = window.document.getElementById("chk_distal_higido");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_higido');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_higido: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_higido: '+b.checked);
    }
}
function chk_distal_mancha_branca_ativa(){
    const b = window.document.getElementById("chk_distal_mancha_branca_ativa");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_mancha_branca_ativa');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_mancha_branca_ativa: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_mancha_branca_ativa: '+b.checked);
    }
}
function chk_distal_mancha_inativa(){
    const b = window.document.getElementById("chk_distal_mancha_inativa");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_mancha_inativa');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_mancha_inativa: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_mancha_inativa: '+b.checked);
    }
}
function chk_distal_lesao_carie_primaria(){
    const b = window.document.getElementById("chk_distal_lesao_carie_primaria");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_lesao_carie_primaria');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_lesao_carie_primaria: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_lesao_carie_primaria: '+b.checked);
    }
}
function chk_distal_lesao_carie_cronica(){
    const b = window.document.getElementById("chk_distal_lesao_carie_cronica");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_lesao_carie_cronica');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_lesao_carie_cronica: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_lesao_carie_cronica: '+b.checked);
    }
}
function chk_distal_restauracao_defeituosa(){
    const b = window.document.getElementById("chk_distal_restauracao_defeituosa");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_restauracao_defeituosa');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_restauracao_defeituosa: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_restauracao_defeituosa: '+b.checked);
    }
}
function chk_distal_restauracao_bom_estado(){
    const b = window.document.getElementById("chk_distal_restauracao_bom_estado");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_restauracao_bom_estado');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_restauracao_bom_estado: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_restauracao_bom_estado: '+b.checked);
    }
}
function chk_distal_necessidade_tratamento_endondontico(){
    const b = window.document.getElementById("chk_distal_necessidade_tratamento_endondontico");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_necessidade_tratamento_endondontico');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_necessidade_tratamento_endondontico: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_necessidade_tratamento_endondontico: '+b.checked);
    }
}
function chk_distal_tratamento_endondontico_concluido_(){
    const b = window.document.getElementById("chk_distal_tratamento_endondontico_concluido_");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_tratamento_endondontico_concluido_');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_tratamento_endondontico_concluido_: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_tratamento_endondontico_concluido_: '+b.checked);
    }
}
function chk_distal_extracao_indicada(){
    const b = window.document.getElementById("chk_distal_extracao_indicada");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_extracao_indicada');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_extracao_indicada: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_extracao_indicada: '+b.checked);
    }
}
function chk_distal_necessidade_protese(){
    const b = window.document.getElementById("chk_distal_necessidade_protese");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_necessidade_protese');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_necessidade_protese: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_necessidade_protese: '+b.checked);
    }
}
function chk_distal_protese_fixa_concluida_satisfatoria(){
    const b = window.document.getElementById("chk_distal_protese_fixa_concluida_satisfatoria");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_protese_fixa_concluida_satisfatoria');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_protese_fixa_concluida_satisfatoria: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_protese_fixa_concluida_satisfatoria: '+b.checked);
    }
}
function chk_distal_ausente(){
    const b = window.document.getElementById("chk_distal_ausente");
    b.checked = !b.checked;
    const a = window.document.getElementById('img_distal_ausente');
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_ausente: '+b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_ausente: '+b.checked);
    }
}
function chk_distal_doenca_periodontal(){
    const a = window.document.getElementById('img_distal_doenca_periodontal');
    const b = window.document.getElementById("chk_distal_doenca_periodontal");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_doenca_periodontal: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_doenca_periodontal: ' + b.checked);
    }
}
function chk_distal_faceta_desgaste(){
    const a = window.document.getElementById('img_distal_faceta_degaste');
    const b = window.document.getElementById("chk_distal_faceta_degaste");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_faceta_degaste: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_faceta_degaste: ' + b.checked);
    }
}
function chk_distal_fratura(){
    const a = window.document.getElementById('img_distal_fratura');
    const b = window.document.getElementById("chk_distal_fratura");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_fratura: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_fratura: ' + b.checked);
    }
}
function chk_distal_selante_fazer(){
    const a = window.document.getElementById('img_distal_selante_fazer');
    const b = window.document.getElementById("chk_distal_selante_fazer");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_selante_fazer: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        a.style.boxShadow = 'none';
        console.log('distal_selante_fazer: ' + b.checked);
    }
}
function chk_distal_selante_satisfatorio(){
    const a = window.document.getElementById('img_distal_selante_satisfatorio');
    const b = window.document.getElementById("chk_distal_selante_satisfatorio");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_selante_satisfatorio: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_selante_satisfatorio: ' + b.checked);
    }
}
function chk_distal_anomalia_de_forma(){
    const a = window.document.getElementById('img_distal_anomalia_de_forma');
    const b = window.document.getElementById("chk_distal_anomalia_de_forma");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_anomalia_de_forma: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_anomalia_de_forma: ' + b.checked);
    }
}
function chk_distal_defeito_de_esmalte(){
    const a = window.document.getElementById('img_distal_defeito_de_esmalte');
    const b = window.document.getElementById("chk_distal_defeito_de_esmalte");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_defeito_de_esmalte: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_defeito_de_esmalte: ' + b.checked);
    }
}
function chk_distal_supranumerario(){
    const a = window.document.getElementById('img_distal_supranumerario');
    const b = window.document.getElementById("chk_distal_supranumerario");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_supranumerario: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_supranumerario: ' + b.checked);
    }
}
function chk_distal_restauracao_protese_concluida(){
    const a = window.document.getElementById('img_distal_restauracao_protese_concluida');
    const b = window.document.getElementById("chk_distal_restauracao_protese_concluida");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_restauracao_protese_concluida: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_restauracao_protese_concluida: ' + b.checked);
    }
}
function chk_distal_tratamento_endondontico_concluido(){
    const a = window.document.getElementById('img_distal_tratamento_endondontico_concluido');
    const b = window.document.getElementById("chk_distal_tratamento_endondontico_concluido");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_tratamento_endondontico_concluido: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_tratamento_endondontico_concluido: ' + b.checked);
    }
}
function chk_distal_calculo_recessao_gengival(){
    const a = window.document.getElementById('img_distal_calculo_recessao_gengival');
    const b = window.document.getElementById("chk_distal_calculo_recessao_gengival");
    b.checked = !b.checked;
    if(b.checked === true ){
        a.style.position = 'relative';
        a.style.bottom = '10px';
        a.style.opacity = '1';
        a.style.boxShadow = '0 0 7px 0 rgba(51, 51, 51, 1)';
        console.log('distal_calculo_recessao_gengival: ' + b.checked);
    }
    else if (b.checked === false){
        a.style.border = '2px solid black'
        a.style.position = 'none';
        a.style.bottom = '0';
        a.style.opacity = '0.5';
        console.log('distal_calculo_recessao_gengival: ' + b.checked);
    }
}