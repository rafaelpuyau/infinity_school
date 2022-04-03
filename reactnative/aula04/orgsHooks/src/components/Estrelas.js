import React, { useState } from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity } from 'react-native';

import Estrela from './Estrela';

// MOVER PARA ESTRELA
// import estrela from '../assets/estrela.png';
// import estrelaCinza from '../assets/estrelaCinza.png';

export default function Estrelas({
    quantidade: quantidadeAntiga,
    editavel = false,
    grande = false,
}) {
    const [ quantidade, setQuantidade ] = useState(quantidadeAntiga);
    // REMOVER NA REFATORAÇÃO
    // const estilos = estilosFuncao(grande); 

    // MOVER PARA ESTRELA
    // const getImage = (index) => {
    //     if(index < quantidade) {
    //         return estrela;
    //     }
    //     return estrelaCinza;
    // }

    const RenderEstrelas = () => {
        const listaEstrelas = [];
        for(let i = 0; i < 5 ; i++) {
            listaEstrelas.push(
                // Para encapsular as estrelas
                // <TouchableOpacity
                //     key={i}
                //     onPress={() => setQuantidade(i + 1)}
                //     disabled={!editavel}
                // >
                //     {/* <Image source={estrela} style={estilos.estrela}/> */}
                //     <Image source={getImage(i)} style={estilos.estrela}/>
                // </TouchableOpacity>
                <Estrela 
                    key={i}
                    onPress={() => setQuantidade(i + 1)}
                    desabilitada={!editavel}
                    preenchida={i < quantidade}
                    grande={grande}
                />
            );
        }

        return listaEstrelas;
    }

    return(
        // <Text>***</Text>
        <View style={estilos.estrelas}>
            <RenderEstrelas />
        </View>
    )
}

// const estilosFuncao = (grande) => StyleSheet.create({
//     estrelas: {
//         flexDirection: 'row',
//     },
//     estrela: {
//         width: grande ? 36 : 16,
//         height: grande ? 36 : 16,
//         marginRight: 2,
//     }
// })
const estilos = StyleSheet.create({
    estrelas: {
        flexDirection: 'row',
    },
})