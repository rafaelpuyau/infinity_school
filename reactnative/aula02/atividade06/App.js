import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TextInput, Button, Pressable } from 'react-native';
import { useState } from 'react';

export default function App() {

  const [name, setName] = useState("");
  const [number, setNumber] = useState(0);

  function sum() {
    setNumber(number + 1);
  }

  function reset() {
    setNumber(0)
  }

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />

      {/* <TextInput 
        value={name}
        onChangeText={(val) => setName(val)}
        onSubmitEditing={() => name.length < 3 ? alert('Epa') : alert('Ae')}
      /> */}

      <Text style={styles.result}>{number}</Text>
      {/* <Button
        title='Add 1'
        onPress={sum}
      /> */}

      <Pressable style={styles.button} onPress={sum}>
        <Text style={styles.text}>
          Super ADD Plus
        </Text>
      </Pressable>

      <Pressable style={styles.reset} onPress={reset}>
        <Text style={styles.text}>
          Reset
        </Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  button: {
      alignItems: 'center',
      justifyContent: 'center',
      paddingVertical: 12,
      paddingHorizontal: 32,
      marginTop: 16,
      borderRadius: 8,
      elevation: 3,
      backgroundColor: '#00AA55',
      width: 200,
  },
  reset: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 12,
    paddingHorizontal: 32,
    marginTop: 16,
    borderRadius: 8,
    elevation: 3,
    backgroundColor: '#FFAA55',
    width: 200,
},
  text: {
      fontSize: 16,
      lineHeight: 21,
      fontWeight: 'bold',
      letterSpacing: 0.25,
      color: '#FFFFFF',
  },
  result: {
    fontSize: 72,
  }
});
