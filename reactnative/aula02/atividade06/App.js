import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';
import { useState } from 'react';

export default function App() {

  const [name, setName] = useState("");
  const [number, setNumber] = useState(0);

  function sum(){
    setNumber(number + 1);
  }

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />

      {/* <TextInput 
        value={name}
        onChangeText={(val) => setName(val)}
        onSubmitEditing={() => name.length < 3 ? alert('Epa') : alert('Ae')}
      /> */}

      <Text>{number}</Text>
      <Button
        title='Add 1'
        onPress={sum}
      />
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
});
