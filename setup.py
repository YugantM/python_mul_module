from distutils.core import setup
setup(
  name = 'mul',         
  packages = ['mul'],   
  version = '1.0',      
  license='MIT',        
  description = 'This package returns addition of two integers.',   
  url = 'https://github.com/yugantm/python_mul_module',   
  download_url = 'https://github.com/yugantm/python_mul_module.git',
  entry_points = {
              'console_scripts': ['mul = mul.__main__:main',],
              },
  scripts=['scripts/mul'],  
  keywords = ['addition', 'calculation'],  
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
