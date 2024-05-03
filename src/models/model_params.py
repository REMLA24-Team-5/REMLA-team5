params = {'loss_function': 'binary_crossentropy',
              'optimizer': 'adam',
              'sequence_length': 200,
              'batch_train': 50,
              'batch_test': 50,
              'categories': ['phishing', 'legitimate'],
              'char_index': None,
              'epoch': 1,
              'embedding_dimension': 50,
              'dataset_dir': "../dataset/small_dataset/"}