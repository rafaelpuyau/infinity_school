import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View } from 'react-native';

// Importando os componentes
import Header from './src/components/Header';
import Footer from './src/components/Footer';

export default function App() {
  return (
    <>
      <StatusBar style="light" />
      <Header title="Infinity School" />
      <View style={styles.container}></View>
      <Footer info="by Rafael Puyau - 2022" />
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#464646',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
