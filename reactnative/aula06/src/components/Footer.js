import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

export default function Footer(props) {
    return(
        <View style={styles.container}>
            <Text style={styles.footer}>
                {props.info}
            </Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: 'tomato',
        // alignItems: 'center',
    },
    footer: {
        fontSize: 12,
        color: '#FFFFFF',
        textAlign: 'center',
        paddingVertical: 16
    }
})