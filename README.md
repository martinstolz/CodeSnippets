# Xcode Code Snippets

### Convenience installation (recommended)
Link code snippets to the appropriate Xcode code snippet folder and install the pre-commit hook which updates the documentation on every commit by running the following command:

    sh .install.sh

### Manual installation
Clone the repository into the following path:

    cd ~/Library/Developer/Xcode/UserData/CodeSnippets
    git clone git@github.com:martinstolz/CodeSnippets.git .

Or link from your cloned folder to the appropriate Xcode code snippet folder by running the following command:

    sh .installLinkage.sh

#### Installing the pre-commit hook
This README is generated automatically using `.generateDescription.py`.
To run this script automatically before each commit, install the pre-commit hook like this:

    python .installPrecommitHook.py

### Snippet Descriptions

**addAChildViewcontroller.codesnippet**  (Add a child ViewController)  
Shortcut: `childViewController`  
Adds a child ViewController to self

    UIViewController *newController = <#newController#>;
        [newController willMoveToParentViewController:self];
        [self addChildViewController:newController];
        [self.contentView addSubview:newController.view];
        [newController didMoveToParentViewController:self];

**assignPropertyDeclaration.codesnippet**  (Assign Property Declaration)  
Shortcut: `propertyAssign`  


    @property (nonatomic, assign) <#type#> <#name#>;

**blockSafeSelfPointer.codesnippet**  (Block Safe Self Pointer)  
Shortcut: `blockSelf`  
A weak pointer to self (for usage in blocks).

    __weak typeof(self) blockSelf = self;

**bundleResourcePath.codesnippet**  (Bundle Resource Path)  
Shortcut: `bundleResourcePath`  


    NSBundle *bundle = [NSBundle mainBundle] pathForResource:<#(NSString *)#> ofType:<#(NSString *)#>];

**classComment.codesnippet**  (Class Comment)  
Shortcut: `commentClass`  
Creates a HeaderDoc like class comment

    /**
        @class
        @abstract
        @discussion
     */

**collectionViewDataSource.codesnippet**  (Collection View Data Source)  
Shortcut: `collectionViewDataSource`  
Creates delegate methods of UICollectionView's data source

    #pragma mark - Collection view data source
    
    - (NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
    {
        <#code#>
    }
    
    - (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (NSInteger)numberOfSectionsInCollectionView:(UICollectionView *)collectionView
    {
        <#code#>
    }
    
    - (UICollectionReusableView *)collectionView:(UICollectionView *)collectionView viewForSupplementaryElementOfKind:(NSString *)kind atIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }

**collectionViewDelegate.codesnippet**  (Collection View Delegate)  
Shortcut: `collectionViewDelegate`  
Creates delegate methods of UICollectionView's delegate

    #pragma mark - Collection view delegate
    
    - (BOOL)collectionView:(UICollectionView *)collectionView shouldHighlightItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView didHighlightItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView didUnhighlightItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (BOOL)collectionView:(UICollectionView *)collectionView shouldSelectItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (BOOL)collectionView:(UICollectionView *)collectionView shouldDeselectItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView didDeselectItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView didEndDisplayingCell:(UICollectionViewCell *)cell forItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView didEndDisplayingSupplementaryView:(UICollectionReusableView *)view forElementOfKind:(NSString *)elementKind atIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (BOOL)collectionView:(UICollectionView *)collectionView shouldShowMenuForItemAtIndexPath:(NSIndexPath *)indexPath
    {
        <#code#>
    }
    
    - (BOOL)collectionView:(UICollectionView *)collectionView canPerformAction:(SEL)action forItemAtIndexPath:(NSIndexPath *)indexPath withSender:(id)sender
    {
        <#code#>
    }
    
    - (void)collectionView:(UICollectionView *)collectionView performAction:(SEL)action forItemAtIndexPath:(NSIndexPath *)indexPath withSender:(id)sender
    {
        <#code#>
    }

**complexMethodComment.codesnippet**  (Complex Method Comment)  
Shortcut: `docMethodComplex`  
Creates a complex HeaderDoc method comment

    /**
        @methodName <#methodName#>
        @abstract   <#abstract#>
        @discussion <#discussion#>
    
        @param      <#param#>
     
        @return     <#return#>
     */

**createAndShowAnUialertview.codesnippet**  (Create & show an UIAlertView)  
Shortcut: `alertview`  
Shows a newly created alertview

    UIAlertView* alertView = [[UIAlertView alloc] initWithTitle:<#title#>
                                                            message:<#message#>
                                                           delegate:<#self#>
                                                  cancelButtonTitle:<#nil#>
                                                  otherButtonTitles:<#@"OK"#>, nil];
        [alertView show];

**createAnUiimageview.codesnippet**  (Create An UIImageView)  
Shortcut: `imageView`  
Inits a new imageView with an image via imageNamed.

    [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"<#imageName#>"]]

**createAReusableUitableviewcell.codesnippet**  (Create A Reusable UITableViewCell)  
Shortcut: `tableViewCell`  
Initialises / deques a new cell from the tableview using an identifier

    // create / dequeue cell
    static NSString* identifier = @"<#identifier#>";
        UITableViewCell* cell = [tableView dequeueReusableCellWithIdentifier:identifier];
        if (cell == nil) {
            cell = [[<#UITableViewCell#> alloc] initWithStyle:<#UITableViewCellStyleSubtitle#> reuseIdentifier:identifier];
        }
        
        return cell;

**dateFormatterAndTimeZone.codesnippet**  (Date Formatter & Time Zone)  
Shortcut: `dateformatter+timezone`  
Used for creating a date formatter converted to a specific timezone

        NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
        dateFormatter.dateFormat = @"yyyy-MM-dd'T'HH:mm";
        
        NSTimeZone *gmt = [NSTimeZone timeZoneWithAbbreviation:@"PST"]; // default is GMT
        [dateFormatter setTimeZone:gmt];
        NSString *timeStamp = [dateFormatter stringFromDate:[NSDate date]];
        [dateFormatter release];
    

**dealloc.codesnippet**  (Dealloc)  
Shortcut: `dealloc`  
Creates the dealloc method

    - (void)dealloc
    {
        <#ivar#>
    }

**delegateCall.codesnippet**  (Delegate Call)  
Shortcut: `delegatecall`  
Creates a delegate call using respondToSelector

    if ([self.delegate respondsToSelector:@selector(<#Selector Signature#>)])
        {
            [self.delegate <#Delegate Method#>];
        }

**elseIfStatement.codesnippet**  (Else If Statement)  
Shortcut: `elseIf`  


    else if (<#expression#>) 
    {
        <#statements#>
    }

**elseStatement.codesnippet**  (Else Statement)  
Shortcut: `else`  


    else
    {
        <#statements#>
    }

**exceptionRaise.codesnippet**  (Exception Raise)  
Shortcut: `exceptionRaise`  


    	[NSException raise:NSInternalInconsistencyException format:@"You must override %@ in a subclass", NSStringFromSelector(_cmd)];

**formattedString.codesnippet**  (Formatted String)  
Shortcut: `stringWithFormat`  
Shortcut for a formatted string

    [NSString stringWithFormat:@"<#string#>", <#param1#>]

**gcd.codesnippet**  (GCD)  
Shortcut: `GCD`  


    dispatch_queue_t mainQueue = dispatch_get_main_queue();
    dispatch_queue_t backgroundQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    //    dispatch_queue_t backgroundQueue = dispatch_queue_create("com.ustwo.something", NULL);  
    
    dispatch_async(backgroundQueue,^{
        
        dispatch_async(mainQueue,^{  
            
        });
    });
    
    // Clean up
    //    dispatch_release(backgroundQueue);
    

**getDocumentsDirectory.codesnippet**  (Get Documents directory)  
Shortcut: `documentsDirectory`  
Create path to documents directory

    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
        NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *filePath = [documentsDirectory stringByAppendingPathComponent:@"<#fileName#>"];

**ifStatement.codesnippet**  (If Statement)  
Shortcut: `if`  


    if (<#condition#>)
    {
        <#statements#>
    }

**importFramework.codesnippet**  (Import Framework)  
Shortcut: `impF`  
import a framework

    #import <<#header#>>

**importHeader.codesnippet**  (Import Header)  
Shortcut: `impH`  
Import a header

    #import "<#header#>"

**incrementingForLoop.codesnippet**  (Incrementing For Loop)  
Shortcut: `forI`  
A For loop incrementing a local variable

    for (NSUInteger i = 0; i < <#count#>; i++)
    {
        <#statements#>
    }

**initalizeAnObject.codesnippet**  (Initalize an object)  
Shortcut: `alloc`  
creates a new object from a given class

    <#ClassName#> *<#variableName#> = [[<#ClassName#> alloc] init];

**initMethod.codesnippet**  (Init Method)  
Shortcut: `init`  


    - (id)init
    {
        self = [super init];
        if (self)
        {
            <#initializations#>
        }
        
        return self;
    }

**initwithframeMethod.codesnippet**  (InitWithFrame Method)  
Shortcut: `initWithFrame`  


    - (id)initWithFrame:(CGRect)frame
    {
        self = [super initWithFrame:frame];
        if (self)
        {
            <#initializations#>
        }
        
        return self;
    }

**initwithnibnameMethod.codesnippet**  (InitWithNibName Method)  
Shortcut: `initWithNibName`  
Safer for instanting UIVIewController's with a nib file based on the class name

    [[<#(Class)#> alloc] initWithNibName:[NSStringFromClass(<#(Class)#>)] bundle:<#(NSBundle *)#>];

**keyValuePairForLocalization.codesnippet**  (Key-Value Pair for Localization)  
Shortcut: `key`  
A localization key and its value

    "<#keyName#>" = "<#value#>";

**kiwiPending.codesnippet**  (Kiwi Pending)  
Shortcut: `kiwiPending`  


    pending(@"should <#message#>", ^{});

**kiwiSpec.codesnippet**  (Kiwi Spec)  
Shortcut: `kiwiSpec`  


    #import "Kiwi.h"
    #import "<#class name#>.h"
    
    SPEC_BEGIN(<#class name#>Spec)
    
    describe(@"<#class name#>", ^{
        __block <#class name#> *<#ivar#> = nil;
        
        beforeEach(^{
            <#ivar#> = [[<#class name#> alloc] init];
        });
        
        afterEach(^{
            [<#ivar#> release];
            <#ivar#> = nil;
        });
        
        pending(@"should <#message#>", ^{});
    });
    
    SPEC_END
    

**localizeAString.codesnippet**  (Localize a string)  
Shortcut: `localizedString`  
Localizes a string from a given key

    NSLocalizedString(@"<#keyName#>", nil)

**pragmaMark.codesnippet**  (Pragma Mark)  
Shortcut: `pragmaMark`  


    #pragma mark - <#Label#>

**privateClassInterface.codesnippet**  (Private Class Interface)  
Shortcut: `privateClassInterface`  


    @interface <#class name#> ()
    <#method#>
    @end

**pushAViewcontroller.codesnippet**  (Push A ViewController)  
Shortcut: `push`  
Pushes a newly created ViewController on the current NavigationController

    <#UIViewController#>* viewController = [[<#UIViewController#> alloc] init];
        [self.navigationController pushViewController:viewController animated:YES];

**retainPropertyDeclaration.codesnippet**  (Retain Property Declaration)  
Shortcut: `propertyRetain`  


    @property (nonatomic, retain) <#type#> <#name#>;

**screenBounds.codesnippet**  (Screen Bounds)  
Shortcut: `screenBounds`  
Get the screen bounds

    CGRect screenBounds = [[UIScreen mainScreen] bounds];

**scrollViewScrollviewdidscroll.codesnippet**  (Scroll View - scrollViewDidScroll)  
Shortcut: `scrollViewDidScroll`  


    - (void)scrollViewDidScroll:(UIScrollView *)scrollView
    {
        <#code#>
    }

**setupAutoresizingOfAView.codesnippet**  (Setup Autoresizing Of A View)  
Shortcut: `autoresizing`  
Set the autoresizing flags of a view

    <#view#>.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;

**simpleMethodComment.codesnippet**  (Simple Method Comment)  
Shortcut: `docMethodSimple`  
Creates a simple HeaderDoc method comment

    /**
     <#method description#>
     
     @param <#param#>
     @return <#returns#>
     */

**singleton.codesnippet**  (Singleton)  
Shortcut: `singleton`  


    + (<#class name#>)sharedInstance
    {
        static dispatch_once_t onceToken = 0;
        __strong static id _sharedObject = nil;
        dispatch_once(&onceToken, ^{
            _sharedObject = [[self alloc] init];
        });
        
        return _sharedObject;
    }

**strongPropertyDeclaration.codesnippet**  (Strong Property Declaration)  
Shortcut: `propertyStrong`  


    @property (nonatomic, strong) <#type#> <#name#>;

**synthesize.codesnippet**  (Synthesize)  
Shortcut: `synthesize`  


    @synthesize <#property#> = _<#propertyIVar#>;

**uitableviewDataSource.codesnippet**  (UITableView Data Source)  
Shortcut: `tableDataSource`  


    #pragma mark - Table view data source
    
    - (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
    {
        return 1;
    }
    
    - (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
    {
        return 1;
    }
    
    - (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
    {
        static NSString *cellIdentifier = @"Cell";
        
        UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:cellIdentifier];
        
        if(cell == nil)
        {
            cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:cellIdentifier];
        }
        
        cell.textLabel.text = [NSString stringWithFormat:@"Cell %d", indexPath.row];
        
        return cell;
    }

**uitableviewDelegate.codesnippet**  (UITableView Delegate)  
Shortcut: `tableDelegate`  


    #pragma mark - UITableView delegate
    
    - (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
    {
        
    }

**uiviewcontrollerAllocation.codesnippet**  (UIViewController allocation)  
Shortcut: `UIViewControllerAllocWithNibName`  
UIViewControllerAllocWithNibName

    [[<#(Class)#> alloc] initWithNibName:NSStringFromClass([<#(Class)#> class]) bundle:<#(NSBundle *)#>];

**viewDidLoad.codesnippet**  (View Did Load)  
Shortcut: `viewDidLoad`  


    - (void)viewDidLoad
    {
        [super viewDidLoad];
        
        <#code#>
    }

**viewWillAppear.codesnippet**  (View Will Appear)  
Shortcut: `viewWillAppear`  


    - (void)viewWillAppear:(BOOL)animated
    {
        [super viewWillAppear:animated];
        
        <#code#>
    }

**weakPropertyDeclaration.codesnippet**  (Weak Property Declaration)  
Shortcut: `propertyWeak`  


    @property (nonatomic, weak) <#type#> <#name#>;

