// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_vpc.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.Vpc {

  /// <summary>Holder for reflection information generated from gcp/gcp_vpc.proto</summary>
  public static partial class GcpVpcReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_vpc.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpVpcReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChFnY3AvZ2NwX3ZwYy5wcm90bxITb2FrOS50eXRob24uZ2NwLnZwYxoTc2hh",
            "cmVkL3NoYXJlZC5wcm90byI9ChtWcGNBY2Nlc3NDb25uZWN0b3JYVGltZW91",
            "dHMSDgoGY3JlYXRlGAEgASgJEg4KBmRlbGV0ZRgCIAEoCSLGAgoSVnBjQWNj",
            "ZXNzQ29ubmVjdG9yEgoKAmlkGAEgASgJEhUKDWlwX2NpZHJfcmFuZ2UYAiAB",
            "KAkSFgoObWF4X3Rocm91Z2hwdXQYAyABKAESFgoObWluX3Rocm91Z2hwdXQY",
            "BCABKAESDAoEbmFtZRgFIAEoCRIPCgduZXR3b3JrGAYgASgJEg8KB3Byb2pl",
            "Y3QYByABKAkSDgoGcmVnaW9uGAggASgJEhEKCXNlbGZfbGluaxgJIAEoCRIN",
            "CgVzdGF0ZRgKIAEoCRJCCgh0aW1lb3V0cxgLIAEoCzIwLm9hazkudHl0aG9u",
            "LmdjcC52cGMuVnBjQWNjZXNzQ29ubmVjdG9yWFRpbWVvdXRzEjcKDXJlc291",
            "cmNlX2luZm8YDCABKAsyIC5vYWs5LnR5dGhvbi5zaGFyZWQuUmVzb3VyY2VJ",
            "bmZvYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts), global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts.Parser, new[]{ "Create", "Delete" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.Vpc.VpcAccessConnector), global::Oak9.Tython.Gcp.Vpc.VpcAccessConnector.Parser, new[]{ "Id", "IpCidrRange", "MaxThroughput", "MinThroughput", "Name", "Network", "Project", "Region", "SelfLink", "State", "Timeouts", "ResourceInfo" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class VpcAccessConnectorXTimeouts : pb::IMessage<VpcAccessConnectorXTimeouts>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<VpcAccessConnectorXTimeouts> _parser = new pb::MessageParser<VpcAccessConnectorXTimeouts>(() => new VpcAccessConnectorXTimeouts());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<VpcAccessConnectorXTimeouts> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.Vpc.GcpVpcReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public VpcAccessConnectorXTimeouts() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public VpcAccessConnectorXTimeouts(VpcAccessConnectorXTimeouts other) : this() {
      create_ = other.create_;
      delete_ = other.delete_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public VpcAccessConnectorXTimeouts Clone() {
      return new VpcAccessConnectorXTimeouts(this);
    }

    /// <summary>Field number for the "create" field.</summary>
    public const int CreateFieldNumber = 1;
    private string create_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Create {
      get { return create_; }
      set {
        create_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "delete" field.</summary>
    public const int DeleteFieldNumber = 2;
    private string delete_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Delete {
      get { return delete_; }
      set {
        delete_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as VpcAccessConnectorXTimeouts);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(VpcAccessConnectorXTimeouts other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Create != other.Create) return false;
      if (Delete != other.Delete) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Create.Length != 0) hash ^= Create.GetHashCode();
      if (Delete.Length != 0) hash ^= Delete.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Create.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Create);
      }
      if (Delete.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Delete);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(VpcAccessConnectorXTimeouts other) {
      if (other == null) {
        return;
      }
      if (other.Create.Length != 0) {
        Create = other.Create;
      }
      if (other.Delete.Length != 0) {
        Delete = other.Delete;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class VpcAccessConnector : pb::IMessage<VpcAccessConnector>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<VpcAccessConnector> _parser = new pb::MessageParser<VpcAccessConnector>(() => new VpcAccessConnector());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<VpcAccessConnector> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.Vpc.GcpVpcReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public VpcAccessConnector() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public VpcAccessConnector(VpcAccessConnector other) : this() {
      id_ = other.id_;
      ipCidrRange_ = other.ipCidrRange_;
      maxThroughput_ = other.maxThroughput_;
      minThroughput_ = other.minThroughput_;
      name_ = other.name_;
      network_ = other.network_;
      project_ = other.project_;
      region_ = other.region_;
      selfLink_ = other.selfLink_;
      state_ = other.state_;
      timeouts_ = other.timeouts_ != null ? other.timeouts_.Clone() : null;
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public VpcAccessConnector Clone() {
      return new VpcAccessConnector(this);
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 1;
    private string id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Id {
      get { return id_; }
      set {
        id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "ip_cidr_range" field.</summary>
    public const int IpCidrRangeFieldNumber = 2;
    private string ipCidrRange_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string IpCidrRange {
      get { return ipCidrRange_; }
      set {
        ipCidrRange_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "max_throughput" field.</summary>
    public const int MaxThroughputFieldNumber = 3;
    private double maxThroughput_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double MaxThroughput {
      get { return maxThroughput_; }
      set {
        maxThroughput_ = value;
      }
    }

    /// <summary>Field number for the "min_throughput" field.</summary>
    public const int MinThroughputFieldNumber = 4;
    private double minThroughput_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double MinThroughput {
      get { return minThroughput_; }
      set {
        minThroughput_ = value;
      }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 5;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "network" field.</summary>
    public const int NetworkFieldNumber = 6;
    private string network_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Network {
      get { return network_; }
      set {
        network_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "project" field.</summary>
    public const int ProjectFieldNumber = 7;
    private string project_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Project {
      get { return project_; }
      set {
        project_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "region" field.</summary>
    public const int RegionFieldNumber = 8;
    private string region_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Region {
      get { return region_; }
      set {
        region_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "self_link" field.</summary>
    public const int SelfLinkFieldNumber = 9;
    private string selfLink_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string SelfLink {
      get { return selfLink_; }
      set {
        selfLink_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "state" field.</summary>
    public const int StateFieldNumber = 10;
    private string state_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string State {
      get { return state_; }
      set {
        state_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "timeouts" field.</summary>
    public const int TimeoutsFieldNumber = 11;
    private global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts timeouts_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts Timeouts {
      get { return timeouts_; }
      set {
        timeouts_ = value;
      }
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 12;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as VpcAccessConnector);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(VpcAccessConnector other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (IpCidrRange != other.IpCidrRange) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(MaxThroughput, other.MaxThroughput)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(MinThroughput, other.MinThroughput)) return false;
      if (Name != other.Name) return false;
      if (Network != other.Network) return false;
      if (Project != other.Project) return false;
      if (Region != other.Region) return false;
      if (SelfLink != other.SelfLink) return false;
      if (State != other.State) return false;
      if (!object.Equals(Timeouts, other.Timeouts)) return false;
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (IpCidrRange.Length != 0) hash ^= IpCidrRange.GetHashCode();
      if (MaxThroughput != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(MaxThroughput);
      if (MinThroughput != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(MinThroughput);
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (Network.Length != 0) hash ^= Network.GetHashCode();
      if (Project.Length != 0) hash ^= Project.GetHashCode();
      if (Region.Length != 0) hash ^= Region.GetHashCode();
      if (SelfLink.Length != 0) hash ^= SelfLink.GetHashCode();
      if (State.Length != 0) hash ^= State.GetHashCode();
      if (timeouts_ != null) hash ^= Timeouts.GetHashCode();
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (IpCidrRange.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(IpCidrRange);
      }
      if (MaxThroughput != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(MaxThroughput);
      }
      if (MinThroughput != 0D) {
        output.WriteRawTag(33);
        output.WriteDouble(MinThroughput);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Name);
      }
      if (Network.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Network);
      }
      if (Project.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(Project);
      }
      if (Region.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(Region);
      }
      if (SelfLink.Length != 0) {
        output.WriteRawTag(74);
        output.WriteString(SelfLink);
      }
      if (State.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(State);
      }
      if (timeouts_ != null) {
        output.WriteRawTag(90);
        output.WriteMessage(Timeouts);
      }
      if (resourceInfo_ != null) {
        output.WriteRawTag(98);
        output.WriteMessage(ResourceInfo);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (IpCidrRange.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(IpCidrRange);
      }
      if (MaxThroughput != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(MaxThroughput);
      }
      if (MinThroughput != 0D) {
        output.WriteRawTag(33);
        output.WriteDouble(MinThroughput);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Name);
      }
      if (Network.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Network);
      }
      if (Project.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(Project);
      }
      if (Region.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(Region);
      }
      if (SelfLink.Length != 0) {
        output.WriteRawTag(74);
        output.WriteString(SelfLink);
      }
      if (State.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(State);
      }
      if (timeouts_ != null) {
        output.WriteRawTag(90);
        output.WriteMessage(Timeouts);
      }
      if (resourceInfo_ != null) {
        output.WriteRawTag(98);
        output.WriteMessage(ResourceInfo);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (IpCidrRange.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IpCidrRange);
      }
      if (MaxThroughput != 0D) {
        size += 1 + 8;
      }
      if (MinThroughput != 0D) {
        size += 1 + 8;
      }
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (Network.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Network);
      }
      if (Project.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Project);
      }
      if (Region.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Region);
      }
      if (SelfLink.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SelfLink);
      }
      if (State.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(State);
      }
      if (timeouts_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Timeouts);
      }
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(VpcAccessConnector other) {
      if (other == null) {
        return;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      if (other.IpCidrRange.Length != 0) {
        IpCidrRange = other.IpCidrRange;
      }
      if (other.MaxThroughput != 0D) {
        MaxThroughput = other.MaxThroughput;
      }
      if (other.MinThroughput != 0D) {
        MinThroughput = other.MinThroughput;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.Network.Length != 0) {
        Network = other.Network;
      }
      if (other.Project.Length != 0) {
        Project = other.Project;
      }
      if (other.Region.Length != 0) {
        Region = other.Region;
      }
      if (other.SelfLink.Length != 0) {
        SelfLink = other.SelfLink;
      }
      if (other.State.Length != 0) {
        State = other.State;
      }
      if (other.timeouts_ != null) {
        if (timeouts_ == null) {
          Timeouts = new global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts();
        }
        Timeouts.MergeFrom(other.Timeouts);
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
          case 18: {
            IpCidrRange = input.ReadString();
            break;
          }
          case 25: {
            MaxThroughput = input.ReadDouble();
            break;
          }
          case 33: {
            MinThroughput = input.ReadDouble();
            break;
          }
          case 42: {
            Name = input.ReadString();
            break;
          }
          case 50: {
            Network = input.ReadString();
            break;
          }
          case 58: {
            Project = input.ReadString();
            break;
          }
          case 66: {
            Region = input.ReadString();
            break;
          }
          case 74: {
            SelfLink = input.ReadString();
            break;
          }
          case 82: {
            State = input.ReadString();
            break;
          }
          case 90: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 98: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
          case 18: {
            IpCidrRange = input.ReadString();
            break;
          }
          case 25: {
            MaxThroughput = input.ReadDouble();
            break;
          }
          case 33: {
            MinThroughput = input.ReadDouble();
            break;
          }
          case 42: {
            Name = input.ReadString();
            break;
          }
          case 50: {
            Network = input.ReadString();
            break;
          }
          case 58: {
            Project = input.ReadString();
            break;
          }
          case 66: {
            Region = input.ReadString();
            break;
          }
          case 74: {
            SelfLink = input.ReadString();
            break;
          }
          case 82: {
            State = input.ReadString();
            break;
          }
          case 90: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.Vpc.VpcAccessConnectorXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 98: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code