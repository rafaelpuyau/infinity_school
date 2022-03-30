import React from 'react';
import { StyleSheet, View,  Image, Text, Dimensions } from 'react-native';

import Texto from './texto';

import topo from '../../assets/topo.png';
import logo from '../../assets/logo.png';

const width = Dimensions.get('screen').width;

export default function Cesta() {
    return(
        <>
            <Image 
                source={topo}
                style={estilos.topo}
            />
            <Text style={estilos.titulo}>Detalhe da Cesta</Text>
            <View style={estilos.cesta}>
                <Texto style={estilos.nome}>Detalhe do Pedido</Texto>
                <View style={estilos.fazenda}>
                    <Image
                            source={logo}
                            style={estilos.imagemFazenda}
                        />
                        <Texto style={estilos.textoFazenda}>Jenny Jack Farm</Texto>
                    </View>
                    <Texto style={estilos.descricao}>
                        Uma cesta com produtos selecionados 
                        cuidadosamente da fazenda direto para 
                        sua cozinha
                    </Texto>
            </View>
        </>
    )
}

const estilos = StyleSheet.create({
    topo: {
        width: '100%',
        height: 578 / 768 * width,
    },
    titulo: {
        width: '100%',
        position: 'absolute',
        fontSize: 16,
        fontWeight: 'bold',
        lineHeight: 26,
        color: '#FFFFFF',
        padding: 16,
        textAlign: 'center',
    },
    cesta: {
        paddingHorizontal: 12,
        paddingVertical: 12,
    },
    nome: {
        color: '#464646',
        fontSize: 26,
        lineHeight: 42,
        fontWeight: 'bold',
    },
    fazenda: {
        flexDirection: 'row',
        alignItems: 'center',
        paddingVertical: 12,
    },
    imagemFazenda: {
        width: 48,
        height: 48,
    },
    textoFazenda: {
        fontSize: 16,
        lineHeight: 26,
        marginLeft: 12,
    },
    descricao: {
        color: '#A3A3A3',
        fontSize: 16,
        lineHeight: 26,
        
    }
})