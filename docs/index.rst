Quick Start
===========

-------------
Prerequisites
-------------

 - `API keys via Cisco API Console <https://pip.pypa.io/en/stable/user_guide/#config-file>`_
    - Required:
       - EOX V5 API
 - Python 3.6+ only

-------
Install
-------

1. Pip Install Package

.. code-block:: shell

    pip install https://github.com/heyglen/cisco_support_api

2. Configure API Keys

.. code-block:: shell

    cisco_support_api config edit

3. Make requests

.. code-block:: shell

    $ cisco_support_api eox by_serial 1234567890
    CISCO7201-RF 2017-09-30

    $ cisco_support_api eox by_serial 1234567890 --verbose
    CISCO7201-RF
            announced = 2011-09-30
            failure_analysis = 2000-01-02
            service_contract_renewal = 2000-01-02
            service_contract_attachment = 2000-01-02
            last_day_of_support = 2017-09-30
            product_bulletin_url = http://www.cisco.com/en/US/prod/collateral/routers/ps341/end_of_life_c51-681414.html
            bulletin_number = RFEOL7682
            product_description = Cisco 7201 Chassis, 1GB, Dual P/S, 256MB Flash REFURBISHED
            updated = 2000-01-02

4. Use as a library

.. code-block:: shell

    python3.6


.. code-block:: python

    import asyncio

    from cisco_support_api import CiscoSupportApi

    support = CiscoSupportApi()

    for record in support.eox.by_serial('1234567890'):
        print(f'{record.product} {record.last_day_of_support}')
