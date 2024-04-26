<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Speech-to-Text using Deep Learning</title>
</head>
<body>
  <h1>Speech-to-Text using Deep Learning</h1>

  <h2>Overview</h2>

  <p>This project is an implementation of a speech-to-text (STT) system using deep learning techniques. The system takes audio samples as input and transcribes them into text. It is based on the DeepSpeech 2 architecture with modifications and enhancements.</p>

  <h2>Requirements</h2>

  <ul>
    <li>Python 3.x</li>
    <li>PyTorch</li>
    <li>torchaudio</li>
    <li>matplotlib</li>
    <li>numpy</li>
    <li>tqdm</li>
    <li>streamlit</li>
  </ul>

  <h2>Data</h2>

  <p>The project uses the <a href="http://www.openslr.org/12/">LibriSpeech dataset</a> for training and testing. The dataset contains approximately 1000 hours of clean speech data, divided into training and test sets.</p>

  <h2>Code Structure</h2>

  <p>The code is organized into several parts:</p>

  <ol>
    <li><strong>Data Preparation:</strong> Preprocessing of audio data and text transformation.</li>
    <li><strong>Modeling:</strong> Definition of the neural network architecture for speech recognition.</li>
    <li><strong>Training:</strong> Training the model on the training dataset.</li>
    <li><strong>Evaluation:</strong> Evaluation of the model's performance on the test dataset.</li>
    <li><strong>Inference:</strong> Transcribing speech to text using the trained model.</li>
    <li><strong>Streamlit App:</strong> Interactive web application for performing speech-to-text conversion.</li>
  </ol>

  <h2>Instructions</h2>

  <ol>
    <li><strong>Data Preparation:</strong>
      <ul>
        <li>Download the LibriSpeech dataset and place it in the specified root path.</li>
        <li>Run the code to preprocess the data and transform text.</li>
      </ul>
    </li>
    <li><strong>Modeling:</strong>
      <ul>
        <li>Define the CNN and RNN layers for the model.</li>
        <li>Configure the hyperparameters such as the number of layers, dimensions, and dropout rate.</li>
      </ul>
    </li>
    <li><strong>Training:</strong>
      <ul>
        <li>Set up the data loaders for training and testing.</li>
        <li>Initialize the model, optimizer, and criterion.</li>
        <li>Train the model using the specified parameters.</li>
      </ul>
    </li>
    <li><strong>Evaluation:</strong>
      <ul>
        <li>Evaluate the trained model on the test dataset.</li>
        <li>Calculate Word Error Rate (WER) and Character Error Rate (CER).</li>
      </ul>
    </li>
    <li><strong>Inference:</strong>
      <ul>
        <li>Use the trained model to transcribe speech into text.</li>
      </ul>
    </li>
    <li><strong>Streamlit App:</strong>
      <ul>
        <li>Run the Streamlit app using the command: <code>streamlit run app.py</code></li>
        <li>Upload an audio file to perform speech-to-text conversion interactively.</li>
      </ul>
    </li>
  </ol>

  <h2>Results</h2>

  <p>After training the model, the WER and CER on the test set were found to be <strong>[0.4826]</strong> and <strong>[0.5896]</strong> respectively.</p>

  <h2>Future Improvements</h2>

  <ul>
    <li>Experiment with different architectures and hyperparameters.</li>
    <li>Explore other datasets for training to improve generalization.</li>
    <li>Fine-tune the model on specific domains for better performance.</li>
    <li>Enhance the Streamlit app with additional features and better UI/UX.</li>
  </ul>

  <h2>Contributors</h2>

  <ul>
    <li>Hakim</li>
  </ul>

  <h2>Acknowledgments</h2>

  <ul>
    <li>This project is inspired by the DeepSpeech 2 architecture.</li>
    <li>Thanks to the creators of the LibriSpeech dataset for providing valuable data.</li>
  </ul>

  <h2>License</h2>

  <p>This project is licensed under <a href="https://opensource.org/licenses/MIT">MIT License</a>.</p>
</body>
</html>
