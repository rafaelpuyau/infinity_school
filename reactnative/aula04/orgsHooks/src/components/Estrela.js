import React from 'react';
import { TouchableOpacity, Image, StyleSheet } from 'react-native';

import estrela from '../assets/estrela.png';
import estrelaCinza from '../assets/estrelaCinza.png';

export default function Estrela({ 
    onPress, 
    desabilitada = true, 
    preenchida, 
    grande = false, 
}) {

    const estilos = estilosFuncao(grande);

    const getImagem = () => {
        if(preenchida) {
            return estrela;
        }
        return estrelaCinza;
    }

    return(
        <TouchableOpacity
            onPress={onPress}
            disabled={desabilitada}
        >
            {/* <Image source={estrela} style={estilos.estrela}/> */}
            <Image source={getImagem()} style={estilos.estrela}/>
        </TouchableOpacity>
    )
}

const estilosFuncao = (grande) => StyleSheet.create({
    estrela: {
        width: grande ? 36 : 16,
        height: grande ? 36 : 16,
        marginRight: 2,
    }
})