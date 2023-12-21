
Custom environments
===================

.. _Custom environments: 

Customising your evnironment is normally acheived in one of two ways:

    * From the options offfered by Websson as Standard via the :ref:`Enviroment Manager <customising>`
    * Directly from the shell/terminal via SSH
    
There is of course nothing to stop you using a combination of the above although care should be taken
when installing additional libraries / packages and should conform with the associated environment framework.

Non public environments
-----------------------

By default all new environments are created as **Public** unless specified otherwise.

This means that anyone with the URL to the environment can access this environment normally via their browser.

Websson offers the ability to create **Non Pulic** or **Private** environments which essentially means that the evinroment 
as a whole is not accessible to anyone without the appropriate authorisation.

In order to make an environment **private** typical **username** and **password** credentials will need to be provided
in order to limit access.

Changing access
---------------






Connecting via SSH
------------------

In order to connect to you environment via SSH you will first need to download the unique SSH key for
your environment.

This is acheived simply by selecting the :ref:`environment <environment>` from the list of environments in the Environment Manager
and slecting the **SSH Key** action button.

Follow the appropriate prompts and be sure to save the SSH Key in a safe place.

Depending on your choice of SSH application you will then be able to connect directly to you environment via 
normal SSH protocols and install any packages / libraries / scripts etc. that you require in order to generate
your applicaiton.



