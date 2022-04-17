import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView } from 'react-native';

import MeuComponente from './MeuComponente';

export default function App() {
  return (
    <View style={styles.container}>
      ''<StatusBar style="light" />
      <Text style={styles.title}>Meu App</Text>

      <ScrollView>
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
        <MeuComponente />
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#2A2A2A',
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 50,
  },
  title: {
    color: '#FFFFFF',
    fontSize: 24,
    marginBottom: 24
  },
});
