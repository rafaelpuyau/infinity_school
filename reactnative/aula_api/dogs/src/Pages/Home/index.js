import React, { useState, useEffect } from 'react';
import {
    View,
    Image,
    Text,
    TouchableOpacity,
    StyleSheet
} from 'react-native';

import api from '../../Services/api';

export default function Home() {
    const[dog, setDog] = useState({});

    useEffect(
        () => {
            getDogImage();
        }, []
    )

    const getDogImage = async () => {
        const {data} = await api.get();
        setDog(data);
    }

    return(
        <View style={styles.container}>
            <Image
                style={styles.puppy}
                source={{uri: dog.message}}
            />
            <TouchableOpacity style={styles.button} onPress={getDogImage}>
                <Text style={styles.label}>Carregar Imagem</Text>
            </TouchableOpacity>
        </View>

    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
    },
    puppy: {
        width: 200,
        height: 200,
    },
    button: {
        marginTop: 16,
        padding: 10,
        backgroundColor: 'navy',
        borderRadius: 5
    },
    label: {
        fontSize: 16,
        color: '#FDFDFD':
    }
})
